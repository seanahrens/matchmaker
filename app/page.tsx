import Header from "@/app/components/header";
import ChatSection from "./components/chat-section";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center gap-10 p-24 bg-gradient-to-r from-cyan-500 to-blue-500">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold text-white">Mark the Hack-a-thon Matchmaker</h1>
        <p className="text-xl text-gray-200">Find project hack-a-thon and startup project collaborators.</p>
        <p className="text-xl text-gray-200">Tell Mark what kind of teammates you are looking for, or project ideas that will excite you.</p>
      </div>
      <ChatSection />
    </main>
  );
}

