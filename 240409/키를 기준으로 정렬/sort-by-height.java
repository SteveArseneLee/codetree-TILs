import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

class Student implements Comparable<Student>{
    String name;
    int height, weight;
    public Student(String name, int height, int weight){
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(Student student){
        return this.height - student.height;
    }

}

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        Student[] students = new Student[n];
        StringTokenizer st;
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int height = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            students[i] = new Student(name, height, weight);
        }
        Arrays.sort(students);

        for (int i = 0; i<n;i++){
            bw.write(students[i].name+ " ");
            bw.write(students[i].height + " ");
            bw.write(students[i].weight+ "\n");
//            System.out.print(students[i].name + " ");
//            System.out.print(students[i].height + " ");
//            System.out.print(students[i].weight + " ");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}