class TimeMap {
    std::unordered_map<string,vector<pair<string,int>>> store;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        this->store[key].push_back({value,timestamp});
    }
    
    string get(string key, int timestamp) {
        if(this->store.find(key) == this->store.end()) return "";
        vector<pair<string,int>>& values = this->store[key];
        string res = "";
        int l = 0, r = values.size()-1;
        while(l <= r){
            int mid = (l + r) >> 1;
            if(values[mid].second <= timestamp){
                res = values[mid].first;
                l = mid + 1;
            }else r = mid - 1;
        }
        return res;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */