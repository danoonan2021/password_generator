import { signIn, signOut, useSession } from "next-auth/react";
import { Box, Button, HStack, Heading, Text } from "@chakra-ui/react";
import Link from 'next/link';

export default function Home() {
  const { data: session } = useSession();

  return (
    <Box padding="2rem" fontFamily="Arial">
      {!session ? (
        <>
          <Heading>Welcome! Please log in</Heading>
          <Button colorScheme="teal" onClick={() => signIn()}>
            Sign in
          </Button>
        </>
      ) : (
        <>
          <Heading>Welcome, {session.user.name}</Heading>
          <Text>Email: {session.user.email}</Text>
          <HStack>
            <Button colorScheme="teal" onClick={() => signOut()}>
                Sign out
            </Button>
            <Link href="/generate">
                <Button label="Generate" colorScheme="teal">
                    Generate Passwords
                </Button>
            </Link>
          </HStack>
        </>
      )}
    </Box>
  );
}
