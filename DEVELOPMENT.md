# ResonantGeoData Development Information

2D/3D/4D Geospatial Data API and Machine Learning System for Evaluation

## Develop with Docker (recommended quickstart)
This is the simplest configuration for developers to start with.

### Initial Setup
1. Run `docker-compose run --rm django ./manage.py migrate`
2. Run `docker-compose run --rm django ./manage.py createsuperuser`
   and follow the prompts to create your own user

### Add Demo Data (Optional)

Please note that the demo data commands need to run in the `celery` docker
image.

Standard demo data for testing:
- Run `docker-compose run --rm celery ./manage.py demo_data`
- Run `docker-compose run --rm celery ./manage.py wasabi`

The `wasabi` data command can take a particularly long time to run as it is
processing large, remote video files.

Cloud hosted satellite imagery:
- Google Cloud hosted Landsat and Sentinel imagery:
  - Landsat: `docker-compose run --rm celery ./manage.py gc_catalog landsat`
  - Sentinel: `docker-compose run --rm celery ./manage.py gc_catalog sentinel`
- S3 Hosted imagery (soon to go offline by June 2021)
  - Run `docker-compose run --rm celery ./manage.py s3_landsat`

For the `gc_catalog` and `s3_landsat` commands, the `-c` argument is optional and
allows you to control how much imagery to ingest; the full dataset can
take a long time to ingest. These routines actually use a subset of the full
catalogs hosted on data.kitware.com; [@banesullivan](https://github.com/banesullivan)
has local scripts to create the subsets of these subsets.

### Run Application
1. Run `docker-compose up`
2. Access the site, starting at http://localhost:8000/admin/
3. When finished, use `Ctrl+C`


### Application Maintenance
Occasionally, new package dependencies or schema changes will necessitate
maintenance. To non-destructively update your development stack at any time:
1. Run `docker-compose pull`
2. Run `docker-compose build --pull --no-cache`
3. Run `docker-compose run --rm django ./manage.py migrate`

## Develop Natively (advanced)
This configuration still uses Docker to run attached services in the background,
but allows developers to run Python code on their native system.

### Initial Setup
1. Run `docker-compose -f ./docker-compose.yml up -d`
2. Install Python 3.8
3. Install
   [`psycopg2` build prerequisites](https://www.psycopg.org/docs/install.html#build-prerequisites)
4. Create and activate a new Python virtualenv
5. Run: `pip install --find-links https://girder.github.io/large_image_wheels -e .[dev,worker]`
6. Run `source ./dev/export-env.sh`
7. Run `./manage.py migrate`
8. Run `./manage.py createsuperuser` and follow the prompts to create your own user

### Run Application
1.  Ensure `docker-compose -f ./docker-compose.yml up -d` is still active
2. Run:
   1. `source ./dev/export-env.sh`
   2. `./manage.py runserver`
3. Run in a separate terminal:
   1. `source ./dev/export-env.sh`
   2. `celery --app rgd.celery worker --loglevel INFO --without-heartbeat`
4. When finished, run `docker-compose stop`

## Remap Service Ports (optional)
Attached services may be exposed to the host system via alternative ports. Developers who work
on multiple software projects concurrently may find this helpful to avoid port conflicts.

To do so, before running any `docker-compose` commands, set any of the environment variables:
* `DOCKER_POSTGRES_PORT`
* `DOCKER_RABBITMQ_PORT`
* `DOCKER_MINIO_PORT`

The Django server must be informed about the changes:
* When running the "Develop with Docker" configuration, override the environment variables:
  * `DJANGO_MINIO_STORAGE_MEDIA_URL`, using the port from `DOCKER_MINIO_PORT`.
* When running the "Develop Natively" configuration, override the environment variables:
  * `DJANGO_DATABASE_URL`, using the port from `DOCKER_POSTGRES_PORT`
  * `DJANGO_CELERY_BROKER_URL`, using the port from `DOCKER_RABBITMQ_PORT`
  * `DJANGO_MINIO_STORAGE_ENDPOINT`, using the port from `DOCKER_MINIO_PORT`

Since most of Django's environment variables contain additional content, use the values from
the appropriate `dev/.env.docker-compose*` file as a baseline for overrides.

## Testing
### Initial Setup
tox is used to execute all tests.
tox is installed automatically with the `dev` package extra.

When running the "Develop with Docker" configuration, all tox commands must be run as
`docker-compose run --rm django tox`; extra arguments may also be appended to this form.

### Running Tests
Run `tox` to launch the full test suite.

Individual test environments may be selectively run.
This also allows additional options to be be added.
Useful sub-commands include:
* `tox -e lint`: Run only the style checks
* `tox -e type`: Run only the type checks
* `tox -e test`: Run only the pytest-driven tests
* `tox -e check-migrations`: Run only the migration tests
* `tox -e format`: Format the code using Black

To automatically reformat all code to comply with
some (but not all) of the style checks, run `tox -e format`.
