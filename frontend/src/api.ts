import axios from "axios";

axios.defaults.baseURL = import.meta.env.VITE_HOST_URL;

interface State {
  image: string;
  frames: number;
  landing_frame?: number;
  left: number;
  right: number;
}

class Api {
  static async play(response: boolean, state: State | object): Promise<State> {
    const result = await axios.post("/", {
      from: "vue",
      state: { ...state, response },
    });
    return result.data;
  }

  static async start(): Promise<State> {
    const response = await axios.post("/", { from: "vue" });
    return response.data;
  }
}

export default Api;
export type { State };
