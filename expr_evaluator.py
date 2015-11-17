
def multiply(a, b):
    return (a * b)


def divide(a, b):
    return (a/b)


expr_map = {
    '*': multiply,
    '/': divide
}


def evaluate(routes, route, value):

    if route not in routes:
        print 'route: ' + str(route) + ' is not configured in routes'

    exp = routes[route]['expr']
    magnitude = routes[route]['magnitude']

    if exp not in expr_map:
        print 'operation not defined for the expression: ' + str(exp)

    method = expr_map[exp]
    result = method(value, magnitude)

    return result
