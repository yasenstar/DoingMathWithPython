        anim = animation.FuncAnimation(
            fig,
            update_points,
            fargs = (x, y, plot),
            frames = len(x),
            interval = 25
        )