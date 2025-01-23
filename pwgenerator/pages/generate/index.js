import { use, useState } from "react";
import { Text, Button, VStack, Heading } from "@chakra-ui/react";
import { supabase } from "@/utils/supabaseClient";
import { useSession } from "next-auth/react";

export default function PasswordGenerator() {
  const [words, setWords] = useState(4);
  const [nums, setNums] = useState(1);
  const [caps, setCaps] = useState(1);
  const [symbols, setSymbols] = useState(1);
  const [password, setPassword] = useState("");

  const { data: session } = useSession();

  const savePassword = async (password) => {
    const { data, error } = await supabase
      .from("passwords")
      .insert([{ password: password, user_email: session.user.email}]);      
  
    if (error) {
      console.error("Error saving password:", error.messages);
    } else {
      console.log("Password saved:", data);
    }
  };
  
  const generatePassword = async () => {
    const response = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ "words":words, "nums":nums, "caps":caps, "symbols":symbols }),
    });
  
    const data = await response.json();
    if (data.password) {
      setPassword(data.password);
      savePassword(data.password);
    } else {
      alert("Error generating password");
    }
  };
  

  return (
    <div>
      <Heading>Generate a Password</Heading>
      <VStack>
        <Text>
          Words: <input type="number" value={words} onChange={(e) => setWords(e.target.value)} />
        </Text>
        <Text>
          Numbers: <input type="number" value={nums} onChange={(e) => setNums(e.target.value)} />
        </Text>
        <Text>
          Capitals: <input type="number" value={caps} onChange={(e) => setCaps(e.target.value)} />
        </Text>
        <Text>
          Symbols: <input type="number" value={symbols} onChange={(e) => setSymbols(e.target.value)} />
        </Text>
        <Button onClick={generatePassword}>Generate</Button>
        {password && <p>Your password: {password}</p>}
      </VStack>
    </div>
  );
}
