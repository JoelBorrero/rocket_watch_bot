import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faAngleRight,
  faFilm,
  faFilter,
  faHandshake,
  faPlay,
  faQuestion,
} from "@fortawesome/free-solid-svg-icons";

library.add(faAngleRight, faFilm, faFilter, faHandshake, faPlay, faQuestion);

export abstract class Icons {
  public static angleRight = "angle-right";
  public static film = "film";
  public static filter = "filter";
  public static handshake = "handshake";
  public static play = "play";
  public static question = "question";
}
