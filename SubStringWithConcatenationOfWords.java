class Solution {
    public List<Integer> findSubstring(String str, String[] words) {
        
        if(str==null||str.length()==0||words == null||words.length==0){
            return new ArrayList<>();
        }
        Map<String ,Integer> frequencyMap = new HashMap<>();
        
        for(String word : words){
            frequencyMap.put(word,frequencyMap.getOrDefault(word,0)+1);
        }
        
        int wordlength = words[0].length();
        int totalwords = words.length;
        List<Integer> result = new ArrayList<>();
        
        for(int i=0;i<=str.length() - wordlength*totalwords;i++){
            HashMap<String ,Integer> seenWords = new HashMap<>();
            for(int j=0;j<totalwords;j++){
                int wordIndex = i+j*wordlength;
                String word = str.substring(wordIndex,wordIndex+wordlength);
                if(!frequencyMap.containsKey(word)){
                    break;
                }
                seenWords.put(word,seenWords.getOrDefault(word,0)+1);
                if(seenWords.get(word)>frequencyMap.getOrDefault(word,0)){
                    break;
                }
                if(j+1==totalwords){
                    result.add(i);
                }
            }
            
        }
        
        return result;
        
    }
}
