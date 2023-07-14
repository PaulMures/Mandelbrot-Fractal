#Name: Mandelbrot Fractal Project
#Date: Started 03/27/2023 - Finished 03/31/2023
#Developer:
#Description: The program draws a fractal. Using a complex point (c) to generate an orbit, the program determines whether or not
            # the orbit is divergent or non-divergent and will then paint a pixel. The fractal is generated within an 800x800 window.

import tkinter

def main():

    window=tkinter.Tk()
    window.geometry("800x800")
    window.title("Mandelbrot Fractal")

    canvas=tkinter.Canvas(window, height = 800, width = 800, bg = 'blue')

    for x in range(1500):

        for y in range(1500):

            #x_o = x + (1 - x) * y/800
            #y_o = y + (1 - y) * x/800
            x_o = x * 1/800 - 2
            y_o = y * 1/800 - 1
            c = complex(x_o,y_o)
            seq = 0
            one_kay = False
            z = 0
            #print(x_o)
            #print(y_o)
            #print(c)

            while seq < 100 and one_kay == False:

                seq = seq + 1
                z = (z * z) + c
                #print(z)
                #print(abs(z))
                #print(seq)
                if abs(z) > 1000:
                    one_kay =  True

            if abs(z) >= 1000:

                if seq <= 25:

                    #print("divergent")
                    dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="black")

                elif seq <= 30:

                    #print("divergent")
                    dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="red")

                elif seq <= 60:

                    #print("divergent")
                    dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="yellow")

                elif seq <= 70:

                    #print("divergent")
                    dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="purple")

                elif seq <= 80:

                    #print("divergent")
                    dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="green")

                elif seq <= 100:

                    #print("divergent")
                    dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="orange")

            elif seq >= 100 and abs(z) < 1000:

                #print("non-divergent")
                dot = canvas.create_line((x-400),(y-400),(x-400)+1,(y-400)+1,fill="white")
                
            #input()


    canvas.pack()
    canvas.update()
    print("done")

    window.mainloop()

main()
