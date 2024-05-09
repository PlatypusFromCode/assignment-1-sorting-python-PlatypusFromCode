def quick_sort(arr: list[int]) -> list[int]:
    if (len(arr) < 2):  # Für den Fall, dass das Array leer ist, oder nur 1 Element
        return arr  # besitzt, müssen wir nix tun und geben es unveränder zurück
    else:

        # pivot-element festlegen, wir beginnen bei 0
        pivot_el = arr[0]

        # restliche elemente von 1 bis ende
        rest_arr = arr[1:]

        # Elemente die kleiner sind als pivot Element
        low_arr = [each for each in rest_arr if each < pivot_el]

        # Elemente die größer sind als pivot Element
        high_arr = [each for each in rest_arr if each >= pivot_el]

        # Jede Liste sortieren, low_arr + pivot_el und high_arr zusammenfassen
    return quick_sort(low_arr) + [pivot_el] + quick_sort(high_arr)  #


def counting_sort(arr: list[int]) -> list[int]:
    # if the array is empty
    if not arr:
        return []
    else:
        # finding the greatest number of an array
        max = arr[0];
        size = len(arr)
        for i in range(0, size):
            if arr[i] >= max:
                max = arr[i]
        print('max', max)

        # creating arrays for counting and sorting

        output = []
        count = [0] * (max + 1)

        # counting the number of each digit

        for i in range(0, size):
            count[arr[i]] += 1
        print(count)

        # building the sorted array

        for i in range(0, len(count)):
            while count[i] > 0:
                output.append(i)
                count[i] -= 1
        return output

