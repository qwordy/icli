Azure CLI kernel for Jupyter Notebook.

Install dependencies.
```
pip install ipykernel
pip install jupyter-console
```

Run `fykernel.py`. You will see something like
```
To connect another client to this kernel, use:
    --existing kernel-24000.json
```

Run
```
jupyter console --existing kernel-24000.json
```