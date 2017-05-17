import java.util.*;
import java.io.*;
import java.util.concurrent.*;

public class DateCount{
	
	public ConcurrentMap<String, Integer> library = new ConcurrentHashMap<>();

	public DateCount(File input){

		try{
			BufferedReader inputRead = new BufferedReader(new FileReader(input));
			while(inputRead.ready()){
                        String line = inputRead.readLine();
                        String word;
                        //String [] words = line.split("\\s+");
                        //String word = words[0];
                        if(line.length() >= 8){
                            word = line.substring(0,8);
                            System.out.println(word);
                        
                        
                            if(library.containsKey(word)){
                            	//System.out.println(word);
                            	int currentCount = library.get(word);
                            	currentCount++;
                            	//System.out.println(currentCount);
                            	library.put(word, currentCount++);
                            	//System.out.println(library.get(word));
                            }
                            else{
                   				library.put(word, 1);
                   			}
                        }
               			
			}
			inputRead.close();
		}         
        catch(IOException e){
            System.out.println("IOException");
            e.printStackTrace();
        }

		 
    }

    public void print(){
		Scanner s = new Scanner(System.in);
        System.out.print("output file name: ");
        String outputFile = s.nextLine();
        PrintWriter writer = null;
        try{
            writer = new PrintWriter(outputFile);
        }
        catch(FileNotFoundException e){
            System.out.println("Writer Failed.");
            System.exit(1);
        }

    	for (String key : library.keySet()) {
    		writer.println(key + ", " + library.get(key));
   			 System.out.println(key + "," + library.get(key));
		}

		writer.close();
    }

	public static void main(String[] args){
		System.out.println("Database name: "+args[0]);
		File input = new File(args[0]);

                //checks to make sure there is a file input
            Scanner in = null;
            try{
                    in = new Scanner(input);
                    System.out.println("Input acceptable!");
            }
            catch(FileNotFoundException e){
                    System.out.println("The file doesn't exist.");
                    System.exit(1);
            }

            DateCount dateCounter = new DateCount(input);
			dateCounter.print();
        }

	

}