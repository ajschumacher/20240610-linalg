import marimo

__generated_with = "0.6.17"
app = marimo.App(width="medium")


@app.cell
def __():
    import numpy as np
    return np,


@app.cell
def __(np):
    A = np.array([[6, 3, 4],
                  [0, 6, 2],
                  [0, 0, 7]])
    print(A)
    return A,


@app.cell
def __(A, np):
    values, vectors = np.linalg.eig(A)
    print(values)
    print(vectors)
    return values, vectors


@app.cell
def __(np, vectors):
    np.linalg.det(vectors)
    return


@app.cell
def __(np, vectors):
    np.linalg.matrix_rank(vectors)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
