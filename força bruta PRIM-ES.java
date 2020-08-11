public class CalculoMDC {
 
    public int mdc(int a, int b) {
        if (b == 0)
            return a;
        else
            return mdc(b, a % b);
    }
 
    /**
     * @param args
     */
    public static void main(String[] args) {
        CalculoMDC e = new CalculoMDC();
        int a = 123456;
        int b = 654321;
        int x = e.mdc(a, b);
        System.out.printf("mdc(%d, %d) = %d : %s %n", a, b, x, x == 1 ? "primos entre si" : "não primos");
        a = 123457;
        b = 754321;
        x = e.mdc(a, b);
        System.out.printf("mdc(%d, %d) = %d : %s %n", a, b, x, x == 1 ? "primos entre si" : "não primos");
    }
 
}