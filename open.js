import http from 'k6/http';
import { sleep } from 'k6';


export default function () {



   http.get('https://test.allapp.link/ZDso88KpZLswB4XoGiRhwm');
  sleep(1);

  const url = 'https://test.allapp.link/event/';

  const payload = JSON.stringify({
    
    "project": "4t2w9mgpDkBHpaVEKTso74",
    "event": "open",
    "link_hash_id": "ZDso88KpZLswB4XoGiRhwm",
    "intent_url": "amsom://aosom.allapp.link/ZDso88KpZLswB4XoGiRhwm",
    "ip_address": "127.0.0.1",
    "operating_system": "Android",
    "operating_system_version": "10.0.0.0",
    "device_model": "ANA-AN00",
    "device_id": "device_18",
    "user_id": "user_09"

  });

  const params = {
    headers: {
      'Content-Type':'application/json',
      'User-Agent':'"Mozilla/5.0 (Linux; Android 10; ANA-AN00 Build/HUAWEIANA-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.26 SP-engine/2.22.0 baiduboxapp/11.26.0.10 (Baidu; P1 10) NABar/1.0"',
      'Authorization':'Bearer GotiEJY2cH3uZs7kxW8XJwZLRg863z'
    },
  };

 

  http.post(url, payload, params);
  sleep(2)
}
