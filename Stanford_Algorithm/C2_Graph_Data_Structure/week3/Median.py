import heapq

def median(input):
    if len(input) <= 1: return input
    output = []
    min_heaq = []
    max_heaq = []
    if input[0] <= input[1]:
        heapq.heappush(max_heaq, -input[0])
        heapq.heappush(min_heaq, input[1])
        output.append(input[0])
        output.append(input[0])
    else:
        heapq.heappush(max_heaq, -input[1])
        heapq.heappush(min_heaq, input[0])
        output.append(input[0])
        output.append(input[1])
    for num in input[2:]:
        if num > min_heaq[0]:
            heapq.heappush(min_heaq, num)
        else:
            heapq.heappush(max_heaq, -num)
        while len(max_heaq) < len(min_heaq):
            item = heapq.heappop(min_heaq)
            heapq.heappush(max_heaq, -item)
        while len(max_heaq) > len(min_heaq) + 1:
            item = -heapq.heappop(max_heaq)
            heapq.heappush(min_heaq, item)
        output.append(-max_heaq[0])
    return output

if __name__ == '__main__':
    input = []
    with open("Median.txt") as f:
        for num in f:
            input.append(int(num))
    output = median(input)
    print(sum(output) % len(input))