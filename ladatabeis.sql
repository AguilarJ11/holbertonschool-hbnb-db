CREATE DATABASE 'ladatabeis';

USE 'ladatabeis'

CREATE TABLE "users" (
  "id" varchar PRIMARY KEY,
  "email" varchar UNIQUE NOT NULL,
  "name" varchar NOT NULL,
  "password" varchar NOT NULL,
  "first_name" varchar NOT NULL,
  "last_name" varchar NOT NULL,
  "is_admin" bool DEFAULT 0,
  "updated_at" datetime NOT NULL,
  "created_at" datetime NOT NULL
);

CREATE TABLE "places" (
  "id" varchar PRIMARY KEY,
  "host_id" varchar UNIQUE NOT NULL,
  "name" varchar NOT NULL,
  "description" varchar NOT NULL,
  "rooms" integer NOT NULL,
  "bathrooms" integer NOT NULL,
  "max_guest" integer NOT NULL,
  "price_per_night" float NOT NULL,
  "latitude" float NOT NULL,
  "longitude" float NOT NULL,
  "city_id" varchar NOT NULL,
  "amenity_id" varchar NOT NULL,
  "created_at" datetime NOT NULL,
  "updated_at" datetime NOT NULL
);

CREATE TABLE "countries" (
  "code" varchar PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "created_at" datetime NOT NULL,
  "updated_at" datetime NOT NULL
);

CREATE TABLE "cities" (
  "id" varchar PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "country_code" varchar UNIQUE NOT NULL,
  "created_at" datetime NOT NULL,
  "updated_at" datetime NOT NULL
);

CREATE TABLE "amenities" (
  "id" varchar PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "created_at" datetime NOT NULL,
  "updated_at" datetime NOT NULL
);

ALTER TABLE "places" ADD FOREIGN KEY ("host_id") REFERENCES "users" ("id");

ALTER TABLE "places" ADD FOREIGN KEY ("city_id") REFERENCES "cities" ("id");

CREATE TABLE "amenities_places" (
  "amenities_id" varchar,
  "places_amenity_id" varchar,
  PRIMARY KEY ("amenities_id", "places_amenity_id")
);

ALTER TABLE "amenities_places" ADD FOREIGN KEY ("amenities_id") REFERENCES "amenities" ("id");

ALTER TABLE "amenities_places" ADD FOREIGN KEY ("places_amenity_id") REFERENCES "places" ("amenity_id");


ALTER TABLE "cities" ADD FOREIGN KEY ("country_code") REFERENCES "countries" ("code");
