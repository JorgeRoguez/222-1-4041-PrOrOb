public class Human{
    //Atttributes / properties
    int born_year = 1970;
    //Methods
    public void say_hello (){
        System.out.println("Hello");
    }

    public String say_hello_user (String user_name){
            return "Hello "+user_name;
    }

    public int born_year(int year){
        return year; 
    }
}