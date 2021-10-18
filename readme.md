Azure CLI kernel for Jupyter Notebook.

Install dependencies.
```
pip install ipykernel
pip install jupyter-console
```

Install kernel.
```
python -m install
```

Run one of them to launch.
```
jupyter lab
jupyter notebook
jupyter console --kernel bash
jupyter qtconsole --kernel bash
```

You can also start kernel and client individually. Run
```
python fykernel.py
```

You will see output like
```
To connect another client to this kernel, use:
    --existing kernel-24000.json
```

Run
```
jupyter console --existing kernel-24000.json
```
