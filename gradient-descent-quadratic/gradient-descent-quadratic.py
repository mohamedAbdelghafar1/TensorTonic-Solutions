def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    
    for i in range(steps):
         f_x=2*a*x0+b
         new_x=x0-lr*f_x
         x0=new_x
    return x0