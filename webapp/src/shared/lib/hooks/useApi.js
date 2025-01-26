import {useState} from "react";
import axios from "axios";
import {API_URL_PATH, token} from "../../config";

export const useApi = () => {
  const [data, setData] = useState()
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchData = async (url, method, requestData = null) => {
    try {
      const { data } = await axios.request({
        url: API_URL_PATH(url),
        method: method,
        headers: {
          'Authorization': `Bearer ${token}`
        },
        data: requestData,
      })

      setData(data);
      setError(null);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  }

  return {data, error, loading, fetchData};
}
