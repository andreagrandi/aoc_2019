import os


def get_layers(image, height, width):
    image_size = height * width
    layers = {}

    # find all image layers
    for i in range(len(image) // image_size):
        index_a = i * image_size
        index_b = (i * image_size) + image_size
        layers[i] = image[index_a:index_b]
    return layers


def get_fewest_zero_digits(layers):
    """
    Return the layer with fewest 0 digits
    """
    # find the layer with fewest 0 digits
    fewest_zero_digits = 0
    for i in range(len(layers)):
        if layers[i].count('0') < layers[fewest_zero_digits].count('0'):
            fewest_zero_digits = i

    return layers[fewest_zero_digits]


def get_stacked_layer(layers, layer_lenght):
    stacked_layer = []

    for i in range(layer_lenght):
        pixel = None
        for x in reversed(range(len(layers))):
            if layers[x][i] == '0' or layers[x][i] == '1':
                pixel = layers[x][i]
        stacked_layer.append(pixel)
    return ''.join(stacked_layer)


def print_stacked_layer(layer, image_height, image_width):
    layer = layer.replace('0', ' ').replace('1', '*')
    for i in range(image_height):
        index_a = i * image_width
        index_b = (i * image_width) + image_width
        print('{0}'.format(layer[index_a:index_b]))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(current_dir + '/inputs/aoc_08_input.txt', 'r') as file:
        data = file.read().replace('\n', '')
        layers = get_layers(data, 6, 25)
        layer = get_fewest_zero_digits(layers)
        n_digits_01 = layer.count('1')
        n_digits_02 = layer.count('2')
        result = n_digits_01 * n_digits_02
        print('Number of 1 * Number of 2: {0}'.format(result))
        layer = get_stacked_layer(layers, 25 * 6)
        print_stacked_layer(layer, 6, 25)
