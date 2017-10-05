
# Hello Rest  
Simple rest application that says hello message
# Tech Stack
+ Spring Boot
+ Java
+ Maven

# Run
Clone the project https://github.com/padmacho/hellorest.git

Move to cloned folder

Run the below commnad to start the app
		mvn spring-boot:run
The above command will download necessary artifacts and starts the embedded tomcat container on 8080 port
# Accessing API
Use curl command to access the api

		curl http://localhost:8080/hello
## Output
		{"text":"Hello Welcome to REST World!!!"}

# Code

```java
package org.eduami.hellorest;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MessageController {

	@RequestMapping("/hello")
	public Message sayHello() {
		return new Message("Hello Welcome to REST World!!!");
	}

}

```

# Prerequisites
+ JDK
+ Maven
