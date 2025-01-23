import { SessionProvider } from "next-auth/react";
import { ChakraProvider } from "@chakra-ui/react";
import { system } from "@chakra-ui/react/preset";
// import "../app/globals.css";  // Your global styles

const theme = {
    config: {
        useSystemColorMode: false,
        initialColorMode: "light", 
        cssVarPrefix: "chakra",
    }
}

function App({ Component, pageProps }) {
  return (
    <SessionProvider session={pageProps.session}>
        <ChakraProvider value={system}>
            <Component {...pageProps} />
        </ChakraProvider>
    </SessionProvider>
  );
}

export default App;