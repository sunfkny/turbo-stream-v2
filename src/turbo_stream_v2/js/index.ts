import { decode } from "./turbo-stream.ts";
import * as stream from "stream";

const webStream = stream.Readable.toWeb(process.stdin) as ReadableStream<Uint8Array>;

const r = await decode(webStream);

process.stdout.write(JSON.stringify(r.value));
