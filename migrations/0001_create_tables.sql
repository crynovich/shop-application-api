-- Migration: create dbo schema and core tables
CREATE SCHEMA IF NOT EXISTS dbo;

CREATE TABLE IF NOT EXISTS dbo.products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC,
    description TEXT
);

CREATE TABLE IF NOT EXISTS dbo.features (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dbo.products_features (
    product_id INTEGER NOT NULL REFERENCES dbo.products(id) ON DELETE CASCADE,
    feature_id INTEGER NOT NULL REFERENCES dbo.features(id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, feature_id)
);
