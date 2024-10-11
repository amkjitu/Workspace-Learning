public class DynamicArray {

    int size;
    int capacity = 10;
    Object[] array;

    DynamicArray() {
        this.array = new Object[capacity];
    }

    DynamicArray(int capacity) {
        this.capacity = capacity;
        this.array = new Object[capacity];
    }

    //Add element
    public void add(Object data) {
        if (size >= capacity) {
            grow();
        }
        array[size] = data;
        size++;
    }

    //Insert element
    // 0 1 2 3
    // a b c d
    // 0 1 2 3 4
    // a a b c d

    public void insert(int index, Object data) {
        if (size >= capacity) {
            grow();
        }
        else if (index >= size) {
            System.err.println("Array index out of bound");
        }
        else {
            //move the elements to the right 
        for (int i = size; i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = data;
        size++;
    }

    }

    //delete element
    // 0 1 2 3
    // a b c d 
    // 0 1 2
    // a c d 
    public void delete(Object data) {
        for (int i = 0; i < size; i++) {
            if (array[i] == data) {
                //move the elements to the left
                for (int j = i; j < size; j++) {
                    array[j] = array[j + 1];
                }
                array[size] = null;
                size--;
                if (size<=(int) (capacity/3)) {
                    shrink();
                }
                break;
            }
        }

    }

    //search element
    public int search(Object data) {
        for (int i = 0; i < size; i++) {
            if (array[i] == data) {
                return i;
            }
        }
        return -1;
    }

    //grow the array capacity
    private void grow() {
        int newCapacity = (int) (2 * capacity);
        Object[] newArray = new Object[newCapacity];

        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        capacity = newCapacity;
        array = newArray;

    }

    private void shrink(){
        int newCapacity = (int) (capacity/2);
        Object[] newArray = new Object[newCapacity];

        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        capacity = newCapacity;
        array = newArray;
    }

    //check isEmpty
    public boolean isEmpty() {
        return size == 0;
    }

    //Convert the object into string
    public String toString() {
        String string = "";
        for (int i = 0; i < capacity; i++) {
            string += array[i] + ", ";
        }
        if (string != "") {
            string = "[" + string.substring(0, string.length() - 2) + "]";
        }
        else {
            string = "[]";
        }
        return string;
    }
    
    
    

}
