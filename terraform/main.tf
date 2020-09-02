terraform {
  backend "remote" {
    hostname      = "app.terraform.io"
    organization  = "ResonantGeoData"

    workspaces {
      name = "ResonantGeoData"
    }
  }
}

provider "aws" {
  region              = "us-east-1"
  allowed_account_ids = ["381864640041"]
  # Must set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY envvars
}

provider "heroku" {
  # Must set HEROKU_EMAIL, HEROKU_API_KEY envvars
}

data "heroku_team" "common" {
  name = "resonantgeodata"
}

resource "aws_route53_zone" "common" {
  name = "resonantgeodata.com"
}

module "django" {
  source  = "girder/django/heroku"
  version = "0.3.0"

  project_slug = "rgd"
  fqdn = "www.${aws_route53_zone.common.name}"
  heroku_team_name = data.heroku_team.common.name
  route53_zone_id = aws_route53_zone.common.id

  # Optional overrides
  # See https://registry.terraform.io/modules/girder/django/heroku/
  # for other possible optional variables
  heroku_app_name = "resonantgeodata"
  storage_bucket_name = "resonantgeodata-files"
  additional_django_vars = {
    DJANGO_S3FF_UPLOAD_STS_ARN = aws_iam_role.storage_upload.arn
  }
  heroku_worker_dyno_quantity = 0
}