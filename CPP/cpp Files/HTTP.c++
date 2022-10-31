// Create a way to send a HTTP request to a server and get a response
// This is a very basic implementation of HTTP

#include <http.h>
#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <wininet.h>

using namespace std;

// Check if the request was successful
bool checkRequest(HINTERNET hRequest) {
    if (hRequest == NULL) {
        cout << "Error: " << GetLastError() << endl;
        return false;
    }
    return true;
}

// Check if the connection was successful
bool checkConnection(HINTERNET hConnect) {
    if (hConnect == NULL) {
        cout << "Error: " << GetLastError() << endl;
        return false;
    }
    return true;
}

// Make function to send a HTTP request
int sendRequest(string url, string request) {
    // Initialize Winsock
    WSADATA wsaData;
    int iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        cout << "WSAStartup failed: " << iResult << endl;
        return 1;
    }

    // Create a handle to the internet
    HINTERNET hInternet = InternetOpen("HTTP", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);
    if (hInternet == NULL) {
        cout << "Error: " << GetLastError() << endl;
        return 1;
    }

    // Create a handle to the connection
    HINTERNET hConnect = InternetConnect(hInternet, url.c_str(), INTERNET_DEFAULT_HTTP_PORT, NULL, NULL, INTERNET_SERVICE_HTTP, 0, 0);
    if (checkConnection(hConnect) == false) {
        return 1;
    }

    // Create a handle to the request
    HINTERNET hRequest = HttpOpenRequest(hConnect, request.c_str(), NULL, NULL, NULL, NULL, INTERNET_FLAG_RELOAD, 0);
    if (checkRequest(hRequest) == false) {
        return 1;
    }

    // Send the request
    if (!HttpSendRequest(hRequest, NULL, 0, NULL, 0)) {
        cout << "Error: " << GetLastError() << endl;
        return 1;
    }

    // Read the response
    char buffer[1024];
    DWORD bytesRead;
    while (InternetReadFile(hRequest, buffer, 1024, &bytesRead) && bytesRead) {
        cout << buffer << endl;
    }

    // Close the handles
    InternetCloseHandle(hRequest);
    InternetCloseHandle(hConnect);
    InternetCloseHandle(hInternet);

    return 0;
}

int main() {
    // Send a GET request
    sendRequest("www.robinhood.com", "GET");

    // Send a POST request
    sendRequest("www.robinhood.com", "POST");
    
    // Send a HEAD request
    sendRequest("www.robinhood.com", "HEAD");
    return 0;
}