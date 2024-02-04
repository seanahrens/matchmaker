import { Check, Copy } from "lucide-react";

import { JSONValue, Message } from "ai";
import Image from "next/image";
import { Button } from "../button";
import ChatAvatar from "./chat-avatar";
import Markdown from "./markdown";
import { useCopyToClipboard } from "./use-copy-to-clipboard";

interface ChatMessageImageData {
  type: "image_url";
  image_url: {
    url: string;
  };
}

// This component will parse message data and render the appropriate UI.
function ChatMessageData({ messageData }: { messageData: JSONValue }) {
  const { image_url, type } = messageData as unknown as ChatMessageImageData;
  if (type === "image_url") {
    return (
      <div className="rounded-md max-w-[200px] shadow-md">
        <Image
          src={image_url.url}
          width={0}
          height={0}
          sizes="100vw"
          style={{ width: "100%", height: "auto" }}
          alt=""
        />
      </div>
    );
  }
  return null;
}

export default function ChatMessage(chatMessage: Message) {
  const { isCopied, copyToClipboard } = useCopyToClipboard({ timeout: 2000 });
  return (
    <div className="flex items-start gap-4 pr-5 pt-5">
      <ChatAvatar role={chatMessage.role} />
      <div className="group flex flex-1 justify-between gap-2">
        <div className="flex-1 space-y-4">
          {chatMessage.data && (
            <ChatMessageData messageData={chatMessage.data} />
          )}
          <Markdown content={formatMarkdown(chatMessage.content)} />
        </div>
        <Button
          onClick={() => copyToClipboard(formatMarkdown(chatMessage.content))}
          size="icon"
          variant="ghost"
          className="h-8 w-8 opacity-0 group-hover:opacity-100"
        >
          {isCopied ? (
            <Check className="h-4 w-4" />
          ) : (
            <Copy className="h-4 w-4" />
          )}
        </Button>
      </div>
    </div>
  );
}

function formatMarkdown(text: string): string {
  // Regex to match URLs that are not already formatted in Markdown
  const urlRegex = /(?<!\!|\]\()((https?:\/\/)[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?)/g;

  // Function to determine if a URL is an image based on common image file extensions
  const isImageUrl = (url: string): boolean => /\.(jpeg|jpg|gif|png|svg|webp)$/.test(url);

  // Replace function that formats URLs
  const replaceFn = (match: string, p1: string, offset: string, string: string): string => {
      // If it's an image URL, format it to display as an image in Markdown
      if (isImageUrl(match)) {
          return `![Image](${match})`;
      }
      // Otherwise, format it as a clickable link in Markdown
      return `[${match}](${match})`;
  };

  // Replace URLs in the text with Markdown format, skipping those already formatted
  return text.replace(urlRegex, replaceFn);
}

