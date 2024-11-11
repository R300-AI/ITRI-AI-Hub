import os, re

def DLAInfo(model):
    result = os.popen(('neuronrt -a %s -d' % model)).read()
    match = re.search('Handle = 0, <(\d+) x (\d+) x (\d+) x (\d+)>', result)
    if match:
        intput_size = ( int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)) )
    else:
        logging.error("FAIL to find input size of model")
        return

    match = re.findall('Handle = ', result.partition("Output")[2])
    if match:
        output_count = len(match)
    else:
        logging.error("FAIL to find output scountize of model")
        return

    return intput_size, [f"output{i}.bin" for i in range(output_count)]
