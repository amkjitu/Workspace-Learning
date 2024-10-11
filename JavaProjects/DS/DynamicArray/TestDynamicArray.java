public class TestDynamicArray {

    public static void main(String[] args) {
        DynamicArray dynamicArray = new DynamicArray(5);
        
        dynamicArray.add("A");
        dynamicArray.add("B");
        dynamicArray.add("C");
        dynamicArray.add("D");
        dynamicArray.add("E");
        dynamicArray.add("F");
        System.out.println("Elements=" + dynamicArray);
        System.out.println("Capacity=" + dynamicArray.capacity);
        System.out.println("Size=" + dynamicArray.size);

        dynamicArray.delete("A");
        dynamicArray.delete("B");
        dynamicArray.delete("C");
        //dynamicArray.delete("D");
        System.out.println("Elements=" + dynamicArray);
        System.out.println("Capacity=" + dynamicArray.capacity);
        System.out.println("Size=" + dynamicArray.size);
        

        //System.out.println("Empty=" + dynamicArray.isEmpty());

        //dynamicArray.insert(2, "Z");
        //System.out.println("Elements=" + dynamicArray);
        //System.out.println("Size=" + dynamicArray.size);
        

        //dynamicArray.delete("B");
        //System.out.println("Elements=" + dynamicArray);
        //System.out.println("Size=" + dynamicArray.size);
        

        //System.out.println("Searche element at in index=" + dynamicArray.search("C"));





    }

}
