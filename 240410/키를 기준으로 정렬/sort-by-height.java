import java.io.*; import java.util.*;

class Student implements Comparable<Student>{
    String name;
    int height, weight;

    public Student(String name, int height, int weight){
        this.name = name;
        this.height=height;
        this.weight=weight;
    }

    @Override
    public int compareTo(Student student){
        return this.height - student.height;
    }
}


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());


        Student[] students = new Student[n];
        for (int i = 0; i<n;i++){
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int height = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            students[i] = new Student(name, height, weight);
        }

        Arrays.sort(students);

        for(int i = 0; i<n;i++){
            bw.write(students[i].name + " ");
            bw.write(students[i].height + " ");
            bw.write(students[i].weight + "\n");
        }


        br.close();         bw.flush();        bw.close();
    }
}