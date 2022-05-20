package ExpertSys.CredRisk;

import java.util.ArrayList;
import java.util.Scanner;

public class CheckCreditRisk {
    public String startDecisionTree(){
        ArrayList<DecisionTreeNode> tree = buildTree();
        Scanner scanf = new Scanner(System.in);
        DecisionTreeNode currentNode;
        int[] allAnswers = new int[4];

        int userInput;

        for (int i=0; i<tree.size(); i++){
            currentNode = tree.get(i);
            System.out.println("~ " + currentNode.getQuestion());
            System.out.println("  " + currentNode.getAnswerHigh());
            System.out.println("  " + currentNode.getAnswerMedium());
            System.out.println("  " + currentNode.getAnswerLow());
            userInput = scanf.nextInt();

            if (userInput == 1 && i==0) // triggered rule1 = IF high income THEN loan approved
                return "* Loan approved. *";
            allAnswers[i] = userInput;
        }

        scanf.close();
        return getMatch(allAnswers);
    }

    private static ArrayList<DecisionTreeNode> buildTree(){
        ArrayList<DecisionTreeNode> tree = new ArrayList<>();

        DecisionTreeNode incomeNode = new DecisionTreeNode(
            0,
            "What is your income range?",
            "[1] High",
            "[2] Medium",
            "[3] Low"
        );
        tree.add(incomeNode);

        DecisionTreeNode referenceNode = new DecisionTreeNode(
            1,
            "What is the status of your references?",
            "[1] Good",
            "[2] Bad",
            "[]"
        );
        tree.add(referenceNode);

        DecisionTreeNode degreeNode = new DecisionTreeNode(
            2,
            "Do you have a bachelor degree or equivalent?",
            "[1] Yes",
            "[2] No",
            "[]"
        );
        tree.add(degreeNode);

        DecisionTreeNode jobNode = new DecisionTreeNode(
            3,
            "Do you have a job?",
            "[1] Yes",
            "[2] No",
            "[]"
        );
        tree.add(jobNode);

        return tree;
    }

    private String getMatch(int[] answerList){
        // int incomeAnswer = answerList[0];
        // int referenceAnswer = answerList[1];
        // int degreeAnswer = answerList[2];
        // int jobAnswer = answerList[3];
        String returnal = " ";

        if (answerList[0] == 3 && answerList[1] == 2){
            // triggered rule7 = IF low income AND bad reference THEN loan not approved
            returnal = "{!} Not approved. REASON: You have low income and bad references.";
        }

        if (answerList[0] == 2){
            if (answerList[2] == 1 && answerList[3] == 1){
                // triggered rule2 = IF medium income AND has bachelor degree AND has job THEN loan approved
                returnal = "* Loan approved *";
            }else if (answerList[2] == 2 && answerList[3] == 2){
                // triggered rule4 = IF medium income AND hasnt degree and hasnt job THEN loan not approved
                returnal = "{!} Not approved. REASON: You dont have a job, neiter a degree and not enough income.";
            }else{
                // rule3 and rule5 are logic suport rules, reference will be the key
                if (answerList[1] == 1){
                    // triggered rule6 = IF low income AND good reference THEN loan approved
                    returnal = "* Loan approved *";
                }else{
                    returnal = "{!} Not approved. REASON: You dont have satisfying income, neither good references.";
                }
            }
        }

        return returnal;
    }
}
