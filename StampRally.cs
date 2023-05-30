using System;

public class Station {
    public bool isStamped = false;
    
    public void VisitStation() {
        isStamped = true;
    }
}

public class AllStations {
    public Station[] stations;

    public AllStations(int stationNum) {
        stations = new Station[stationNum]; // 配列を初期化

        for (int i = 0; i < stations.Length; i++) {
            stations[i] = new Station(); // 配列の各要素に Station オブジェクトを割り当てる
        }
    }
    
    public bool GetAllStationsStamped() {
        int i = 0;
        for(i = 0; i < stations.Length; i++) {
            if (!stations[i].isStamped) {
                return false;
            }
        }
        // System.Console.WriteLine("All Stations visited!!\n");
        
        return true;
    }
}

public class StampRally {
    static int stationNum = 29;
    
    
    public static void Main() {
        int nowRallyNum = 0;
        int maxRallyNum = 1000;
        int[] lastStationNums;
        int[] stationTimes;
        
        lastStationNums = new int[maxRallyNum];
        stationTimes = new int[stationNum];
        
        StampRally stampRally = new StampRally(); // StampRally クラスのインスタンスを作成
        while(!(nowRallyNum==maxRallyNum)){
            lastStationNums[nowRallyNum]=stampRally.DoARally();
            nowRallyNum++;
        }
        
        foreach(int lastStationNum in lastStationNums){
            // System.Console.Write("{0},", lastStationNum);
            stationTimes[lastStationNum] ++;
        }
        
        System.Console.Write("\n\n");
        
        foreach(int stationTime in stationTimes){
            System.Console.Write("{0},",stationTime);
        }
    }
    
    public int DoARally() {
        int currentStation = 0;
        int times = 0;
        
        
        StampRally stampRally = new StampRally(); // StampRally クラスのインスタンスを作成
        AllStations allStations = new AllStations(stationNum);
        
        allStations.stations[0].VisitStation();
        
        while(!allStations.GetAllStationsStamped()){
            
            if(stampRally.CoinFlip()){ // インスタンスを使用して CoinFlip() メソッドにアクセス
                currentStation ++;
            } else {
                currentStation --;
            }
            
            if(currentStation==-1){     //currentStationを0から駅の数の-1までに収める
                currentStation=stationNum - 1;
            }else if(currentStation==stationNum){
                currentStation=0;
            }
            
            allStations.stations[currentStation].VisitStation();
            times++;
        }
        // System.Console.WriteLine("Last Station Number:{0}\n", currentStation);
        // System.Console.WriteLine("times:{0}\n", times);
        return currentStation;
    }
    
    public bool CoinFlip() {
        Random random = new Random();
        if(random.Next(0,2)==1) {
            // System.Console.WriteLine("Coin flipped:inside\n");
            return true;
        } else {
            // System.Console.WriteLine("Coin flipped:outside\n");
            return false;
        }
    }
}
