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
def __(A, np):
    A @ np.transpose(A)
    return


@app.cell
def __(A, np):
    np.linalg.eig(np.transpose(A) @ A)
    return


@app.cell
def __(A, np):
    np.transpose(A) @ A
    return


@app.cell
def __(A, np):
    np.linalg.eig(A @ np.transpose(A))
    return


@app.cell
def __(A, np):
    left, singular, right = np.linalg.svd(A)
    print(left)
    print(singular)
    print(right)
    return left, right, singular


@app.cell
def __(left, np, right, singular):
    left @ np.diag(singular) @ right
    return


@app.cell
def __(left, np):
    left @ np.transpose(left)
    return


@app.cell
def __(np, right):
    right @ np.transpose(right)
    return


@app.cell
def __(np):
    np.linalg.inv(np.array([[1, 2], [3, 4]]))
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
