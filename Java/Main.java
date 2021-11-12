package classes;

import classes.Course;

public class Main {
    
    public Main(){

    }
    public static void main(String[] args) {
        var obj=new Course("40142", "Pr Or Ob", "Luis Guerra", "5202", "Martes", "19:00 - 20:30");
        obj.bienvenida();
    }
    
}
