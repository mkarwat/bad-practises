from functions import calculatePi, PiContainer, enumarate, printElements
import pathlib as Path

if __name__ == "__main__":
    try:
        myPi01 = PiContainer()
        myPi02 = PiContainer()
        myPi03 = PiContainer()
        piGen01 = calculatePi(5)

        for _ in range(5):
            myPi01.mth(next(piGen01))

    except Exception as e:
        print(f'Something went horribly wrong: {e}')
        
        piGen02 = calculatePi(194)

        for _ in range(23):
            myPi02.mth(next(piGen02))

        piGen03 = calculatePi(6)
        myPi03.mth([i for i in list(piGen03)])

        print(f'My first pi: {printElements(myPi01)}')
        print(f'My second pi: {enumarate(myPi02)}')
        print(f'My third pi: {myPi03.a}')

        # Specify the file path
        file_path = Path('some-file.txt')

        # Writing to a file
        with file_path.open('w') as new_file:
            new_file.write(f'My best pi: {myPi03.a[-2]}')
    
    
