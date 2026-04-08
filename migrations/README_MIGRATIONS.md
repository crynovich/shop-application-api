This folder contains simple SQL migrations and a runner.

To apply migrations locally:

1. Ensure environment variables and `POSTGRES_PASSWORD_FILE` are set as in the project.
2. Activate the virtualenv.
3. Run:

```
python -m migrations.apply_migrations
```

The runner will apply all `*.sql` files in this directory in filename order.
