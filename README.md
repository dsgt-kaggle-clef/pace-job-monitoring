# pace-job-monitoring

Scripts for monitoring PACE jobs.

## generate a report

You can generate a report from a directory of report logs.
Only logs from the relevant array job should be included in the directory.
They should have the following structure:

```
Report-2866632.log
Report-2866632-nvidia-logs.ndjson
Report-2866632-nvidia-logs-processes.csv
Report-2866632-nvidia-logs-utilization.csv
Report-2866632-nvidia-logs-utilization.png
```

We look for reports that match `Report-(\d+)\.(log|out)`.
You may use either of the following sbatch parameters to generate the job.

```bash
#SBATCH --output=Report-%j.log
#SBATCH --output=Report-%j.out
```

Enter an interactive sesssion:

```bash
scripts/salloc
```

Then run the build-report command:

```bash
./scripts/build-report <log_path> <output_path> [overwrite: (true|false)]
```

Assume the output path is set to ~/scratch/my-report

If you can port-forward (such as the automatic port-forwarding in vs-code), then you can preview your report with python:

```bash
python -m http.server --directory ~/scratch/my-report 8888
```

Then review the report on port 8888.
You can upload the site to static site hosting like netlify.
First scp your files over to your local directory:

```bash
scp -r <user>@login-phoenix.pace.gatech.edu:~/scratch/my-report ./my-report/
```

Then upload the folder to https://app.netlify.com/drop.
