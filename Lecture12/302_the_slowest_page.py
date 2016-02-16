import re
from urllib.parse import urlparse

try:
    file_name = 'takovata-access.log'
    result_elements = {}
    with open(file_name, encoding='utf-8') as f:
        previous_temp = None
        for line in f:
            line = line.strip()
            if line:
                line_elements_couples = re.findall(r'(\w+)="(.*?)"', line)
                properties = {}
                for key, value in line_elements_couples:
                    properties[key] = value

                url_elements = urlparse(properties['url'])
                url = url_elements.path
                end = url[-4:]
                if end == '/ws/':
                    continue

                if url in result_elements:
                    result_elements[url].append(float(properties['resp_t']))
                else:
                    result_elements[url] = [float(properties['resp_t'])]

    sorted_results = sorted(result_elements.items(), key=lambda kv: sum(kv[1]) / len(kv[1]), reverse=True)
    print(sorted_results[0][0])
    print("{:.3f}".format(sum(sorted_results[0][1]) / len(sorted_results[0][1])))
except:
    print("INVALID INPUT")