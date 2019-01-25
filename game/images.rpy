init:
    transform lpos:
        xalign 0.2

    transform rpos:
        xalign 0.8

    transform llpos:
        xalign 0.1

    transform rrpos:
        xalign 0.9

    transform lturn:
        align (0.5,0.5)
        linear 27.0 rotate -90
        rotate 0
        repeat
        pass

    transform rturn:
        align (0.5,0.5)
        linear 5.0 rotate 90
        rotate 0
        repeat
        pass

    image bg black:
        "#000"

    #TODO: turn this into arguments? (so I can easily change the rotational speed)
    image blessed:
        size (300,300)
        contains:
            "plus.png"
            rturn

        contains:
            "plus.png"
            lturn

        contains:
            im.MatrixColor("plus.png", im.matrix.colorize("#00f","#fff"))
            additive 1.0
            rturn

        contains:
            im.MatrixColor("plus.png", im.matrix.colorize("#f00","#fff"))
            additive 1.0
            lturn


    image charmed:
        subpixel True
        contains:
            "plus.png"
            rturn

        contains:
            "plus.png"
            lturn

        contains:
            im.MatrixColor("plus.png", im.matrix.colorize("#f00","#fff"))
            additive 1.0
            rturn

        contains:
            im.MatrixColor("plus.png", im.matrix.colorize("#0f0","#fff"))
            additive 1.0
            lturn

    image hexed:
        subpixel True
        contains:
            "plus.png"
            rturn

        contains:
            "plus.png"
            lturn

        contains:
            im.MatrixColor("plus.png", im.matrix.colorize("#0f0","#fff"))
            additive 1.0
            rturn

        contains:
            im.MatrixColor("plus.png", im.matrix.colorize("#00f","#fff"))
            additive 1.0
            lturn
    image strange:
        subpixel True
        im.MatrixColor("plus.png", im.matrix.colorize("#000","#fff"))
        yalign 0.3
        linear 20.0 rotate 360
        rotate 0
        repeat
