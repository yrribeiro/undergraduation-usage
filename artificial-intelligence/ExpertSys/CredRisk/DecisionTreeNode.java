package ExpertSys.CredRisk;

public class DecisionTreeNode {
    public int nodeId;
    public String question;
    public String answerHigh;
    public String answerMedium;
    public String answerLow;

    public DecisionTreeNode(int nodeId, String question, String answerHigh, String answerMedium, String answerLow){
        this.nodeId = nodeId;
        this.question = question;
        this.answerHigh = answerHigh;
        this.answerMedium = answerMedium;
        this.answerLow = answerLow;
    }

    public int getNodeId() {
        return nodeId;
    }

    public void setNodeId(int nodeId) {
        this.nodeId = nodeId;
    }

    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public String getAnswerHigh() {
        return answerHigh;
    }

    public void setAnswerHigh(String answerHigh) {
        this.answerHigh = answerHigh;
    }

    public String getAnswerMedium() {
        return answerMedium;
    }

    public void setAnswerMedium(String answerMedium) {
        this.answerMedium = answerMedium;
    }

    public String getAnswerLow() {
        return answerLow;
    }

    public void setAnswerLow(String answerLow) {
        this.answerLow = answerLow;
    }
}
