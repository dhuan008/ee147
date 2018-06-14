from kernels.black_and_white import blackWhite, CudablackWhite
from kernels.blur import blur

def main():
    blackWhite('imageTest.jpg', 'imageBW.jpg', log = 1)
    CudablackWhite('imageTest.jpg', 'imageCudaBW.jpg', log = 1)


if __name__=="__main__":
    main()