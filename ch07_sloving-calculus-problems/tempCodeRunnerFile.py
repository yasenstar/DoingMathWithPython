            print('{0}: {1:.5f}'.format(var.name, var_max))
            print('Maximum Range: {0:.5f}'.format(f.subs({var:var_max})))