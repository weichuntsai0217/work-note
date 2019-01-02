# Assume you just recorded 2 raw data logs `Log1/` and `Log2/` and they are in `/Users/jimmy_tsai/sdk/`
* I want to clean the redundant path before `IMG/` in `driving_log.csv` of `Log1/` and `Log2`
  - Step 1. Go to `${project_root}/process_data`
  - Step 2. Run `./cln_data.sh /Users/jimmy_tsai/sdk/`
  - Step 3. You would find new `Log1/` and `Log2/` in `/Users/jimmy_tsai/sdk/cleaned_data` whose path contents of `driving_log.csv` is simplified into `IMG/eagle....`
  - Note: `./cln_data.sh` would remove `cleaned_data/` in your data source directory first and then do clean later.

* I want to compress raw logs into `*.tar.gz`
  - Step 1. Go to `${project_root}/process_data`
  - Step 2. Run `./tgz_data.sh /Users/jimmy_tsai/sdk/`
  - Step 3. You would find `Log1.tar.gz` and `Log2.tar.gz` in `/Users/jimmy_tsai/sdk/`

* I want to clean and compress raw logs into `*.tar.gz`
  - Step 1. Go to `${project_root}/process_data`
  - Step 2. Run `./combo_arv_data.sh /Users/jimmy_tsai/sdk/`
  - Step 3. You would find `Log1.tar.gz` and `Log2.tar.gz` in `/Users/jimmy_tsai/sdk/cleaned_data/`

* I want to clean and compress raw logs into `*.tar.gz` and merge `*.tar.gz` into `${projcer_root}/app/data/`
  - Step 1. Go to `${project_root}/process_data`
  - Step 2. Run `./combo_exp_data.sh /Users/jimmy_tsai/sdk/`
  - Step 3. The result would be in `${projcer_root}/app/data/` and then you can run `python model.py` in your dev container.
