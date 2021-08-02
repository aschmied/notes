# Maven

## Get help

* Get help: `mvn help:describe -Dplugin=<group-id>:<artifact-id> -Ddetail`
* See lifecycle: `mvn plan:plan -Dgoals=install` # lines are [phsace] plugin:goal (id)
* Show dependency tree: `mvn dependency:tree`
* Evaluate expression: `mvn help:evaluate ${project.build.sourceDirectory}`

## Building

* Sort pom after update: `mvn sortpom:sort`
* Build single subproject: `mvn clean install -pl :<subproject-name>`
* Run a particular version of a mojo. `mvn <group-id>:<plugin-artifact-id>:<version>:<mojo>`

## Testing

* Run a single test with `mvn test -Dtest=<test-class-name> -pl <group-id>:<artifact-id>`
* Try `mvn clean` if tests fail with unresolved symbols (specifically maven could not find symbols in a test-scoped dependency)

## Dependencies

* Upgrade: `mvn versions:update-properties versions:update-parent versions:use-latest-versions -P update-all`. Optional `-U` to update from remotes
* Fetch dependency source Jars: `mvn dependency:sources -U`
 * Download a particular artifact: `mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:copy -Dartifact=<group-id>:<artifact-id>:RELEASE:jar:jar-with-dependencies -DoutputDirectory=. -Dmdep.stripVersion=true`
