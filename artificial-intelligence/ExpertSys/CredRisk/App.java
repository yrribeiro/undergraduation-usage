package ExpertSys.CredRisk;

public class App{
    public static void main(String[] args) throws Exception{
        CheckCreditRisk app = new CheckCreditRisk();
        System.out.println("\n" + app.startDecisionTree() + "\n");
    }
}