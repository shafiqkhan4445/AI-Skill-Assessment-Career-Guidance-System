# assessment.py - adaptive difficulty assessment

SKILL_LABELS = {
    "python": "Python",
    "sql": "SQL",
    "excel": "Excel",
    "data visualization": "Data Visualization",
    "statistics": "Statistics",
    "html": "HTML",
    "css": "CSS",
    "javascript": "JavaScript",
    "react": "React",
    "java": "Java",
    "databases": "Databases",
    "machine learning": "Machine Learning",
}

BRANCH_SKILL_LABELS = {
    "CSE": dict(SKILL_LABELS),
    "ISE": dict(SKILL_LABELS),
    "ECE": {
        "c programming": "C Programming",
        "python": "Python",
        "circuit analysis": "Circuit Analysis",
        "digital electronics": "Digital Electronics",
        "analog electronics": "Analog Electronics",
        "signals and systems": "Signals & Systems",
        "communication systems": "Communication Systems",
        "microcontrollers": "Microcontrollers",
        "embedded systems": "Embedded Systems",
        "vlsi basics": "VLSI Basics",
        "matlab": "MATLAB / Simulation",
        "pcb design": "PCB Design & Debugging",
    },
}

# We map confidence ratings to practical question difficulty bands.
# 1-2 = Beginner, 3 = Intermediate, 4-5 = Advanced.
DIFFICULTY_MAP = {
    1: "beginner",
    2: "beginner",
    3: "intermediate",
    4: "advanced",
    5: "expert",
}


def _q(skill, difficulty, question, options, answer):
    return {
        "skill": skill,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "answer": answer,  # 1-based option index
    }


QUESTION_BANK = {
    # ------------------------------------------------------------------
    # PYTHON
    # ------------------------------------------------------------------
    "python": {
        "beginner": [
            _q("python", "beginner", "Which keyword is used to define a function in Python?", ["function", "def", "define", "fun"], 2),
            _q("python", "beginner", "Which symbol starts a single-line comment in Python?", ["//", "#", "<!--", "**"], 2),
            _q("python", "beginner", "Which function returns the number of items in a list?", ["count()", "size()", "len()", "length()"], 3),
            _q("python", "beginner", "Which Python type stores key-value pairs?", ["List", "Tuple", "Dictionary", "Set"], 3),
            _q("python", "beginner", "Which value represents a boolean false value?", ["0", "False", "NoneType", "Empty"], 2),
        ],
        "intermediate": [
            _q("python", "intermediate", "Which expression creates a list containing the squares of 1, 2 and 3?", ["[x*x for x in range(1,4)]", "[x^2 for x in 1..3]", "square(1,2,3)", "[1..3]^2"], 1),
            _q("python", "intermediate", "What does the // operator do in Python?", ["True division", "Floor division", "Exponentiation", "Modulus"], 2),
            _q("python", "intermediate", "Which construct is normally used to handle an exception?", ["try/except", "if/else", "for/while", "match/case only"], 1),
            _q("python", "intermediate", "What is a key property of a Python set?", ["It preserves duplicate values", "It stores only unique values", "It stores only strings", "It is ordered by index"], 2),
            _q("python", "intermediate", "What does a lambda expression create?", ["A class", "An anonymous function", "A loop", "A module"], 2),
        ],
        "advanced": [
            _q("python", "advanced", "Which keyword is used to produce values lazily from a generator?", ["yield", "return", "await", "lazy"], 1),
            _q("python", "advanced", "What does the 'is' operator primarily compare?", ["Value equality", "Object identity", "Data types only", "String length"], 2),
            _q("python", "advanced", "What is a common issue with using a mutable list as a default function argument?", ["It causes syntax errors", "The same list can be reused across calls", "It makes the function private", "It disables recursion"], 2),
            _q("python", "advanced", "Which syntax is used to apply a decorator to a function?", ["@decorator", "#decorator", "decorator()", "&decorator"], 1),
            _q("python", "advanced", "Which concept lets a class reuse or extend another class's behavior?", ["Inheritance", "Indexing", "Serialization", "Slicing"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # JAVA
    # ------------------------------------------------------------------
    "java": {
        "beginner": [
            _q("java", "beginner", "Which keyword is used to create an object in Java?", ["class", "new", "object", "create"], 2),
            _q("java", "beginner", "Which method is the usual entry point of a Java application?", ["start()", "run()", "main()", "execute()"], 3),
            _q("java", "beginner", "Which type is used to store a whole number such as 25?", ["int", "char", "boolean", "double"], 1),
            _q("java", "beginner", "Which keyword is used to define a class?", ["object", "class", "struct", "type"], 2),
            _q("java", "beginner", "Which statement prints text to the console?", ["System.out.println()", "print.console()", "Console.write()", "echo()"], 1),
        ],
        "intermediate": [
            _q("java", "intermediate", "What is method overriding?", ["Defining a method with the same signature in a subclass", "Creating two variables with the same name", "Calling a private method", "Deleting a parent method"], 1),
            _q("java", "intermediate", "Which collection provides a resizable array implementation?", ["HashSet", "ArrayList", "TreeMap", "Queue"], 2),
            _q("java", "intermediate", "Which keyword makes a variable belong to the class rather than each object?", ["final", "static", "this", "super"], 2),
            _q("java", "intermediate", "Which feature allows a class to implement multiple contracts?", ["Multiple inheritance through classes", "Interfaces", "Packages", "Constructors"], 2),
            _q("java", "intermediate", "Which block is used to handle an exception?", ["catch", "switch", "assert", "package"], 1),
        ],
        "advanced": [
            _q("java", "advanced", "Which mechanism enables runtime method selection when using a parent reference?", ["Dynamic method dispatch", "Compile-time constants", "Package import", "Method hiding only"], 1),
            _q("java", "advanced", "Which type is commonly used for key-value storage with average constant-time lookup?", ["HashMap", "ArrayList", "Stack", "LinkedList"], 1),
            _q("java", "advanced", "Why are Java String objects considered immutable?", ["Their contents cannot be changed after creation", "They cannot be compared", "They are always stored on disk", "They cannot be concatenated"], 1),
            _q("java", "advanced", "Which is a checked exception example?", ["IOException", "NullPointerException", "ArithmeticException", "ArrayIndexOutOfBoundsException"], 1),
            _q("java", "advanced", "What is polymorphism in object-oriented Java?", ["One interface/reference supporting multiple implementations", "Keeping data private", "Creating many packages", "Compiling code twice"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # SQL
    # ------------------------------------------------------------------
    "sql": {
        "beginner": [
            _q("sql", "beginner", "Which SQL command is used to retrieve data from a table?", ["INSERT", "UPDATE", "SELECT", "DELETE"], 3),
            _q("sql", "beginner", "Which clause filters rows in a query?", ["WHERE", "FROM", "ORDER BY", "GROUP BY"], 1),
            _q("sql", "beginner", "Which command adds a new row to a table?", ["ADD", "INSERT", "CREATE", "APPEND"], 2),
            _q("sql", "beginner", "Which constraint uniquely identifies a row?", ["FOREIGN KEY", "PRIMARY KEY", "CHECK", "DEFAULT"], 2),
            _q("sql", "beginner", "Which function counts rows?", ["SUM()", "COUNT()", "TOTAL()", "ROWS()"], 2),
        ],
        "intermediate": [
            _q("sql", "intermediate", "Which clause groups rows before aggregate calculations?", ["GROUP BY", "ORDER BY", "WHERE", "DISTINCT"], 1),
            _q("sql", "intermediate", "Which JOIN returns matching rows from both tables?", ["INNER JOIN", "FULL JOIN", "CROSS JOIN", "SELF JOIN only"], 1),
            _q("sql", "intermediate", "Which clause filters grouped results after aggregation?", ["WHERE", "HAVING", "GROUP BY", "LIMIT"], 2),
            _q("sql", "intermediate", "Which command modifies existing rows?", ["UPDATE", "ALTER", "MERGE", "CHANGE"], 1),
            _q("sql", "intermediate", "What is a subquery?", ["A query nested inside another query", "A backup table", "A database schema", "A stored password"], 1),
        ],
        "advanced": [
            _q("sql", "advanced", "Which feature can calculate a running total without collapsing rows?", ["Window function", "GROUP BY", "DISTINCT", "UNION"], 1),
            _q("sql", "advanced", "What is a common benefit of a database index?", ["Faster lookup for suitable queries", "More duplicate rows", "Automatic normalization", "Eliminating all storage cost"], 1),
            _q("sql", "advanced", "What does a CTE provide?", ["A named temporary result set within a query", "A permanent backup database", "A network connection", "A user account"], 1),
            _q("sql", "advanced", "Why should an UPDATE usually include a WHERE clause when only some rows should change?", ["To limit which rows are modified", "To enable joins", "To create a primary key", "To sort the table"], 1),
            _q("sql", "advanced", "What problem can poor transaction design lead to?", ["Lost updates or inconsistent data", "Automatic data compression", "Faster rendering", "CSS conflicts"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # EXCEL
    # ------------------------------------------------------------------
    "excel": {
        "beginner": [
            _q("excel", "beginner", "Which Excel function adds numbers in a range?", ["SUM", "COUNT", "TOTAL", "ADD"], 1),
            _q("excel", "beginner", "Which function returns the average of numbers?", ["MEAN", "AVG", "AVERAGE", "MID"], 3),
            _q("excel", "beginner", "What does a cell reference such as B4 identify?", ["A worksheet name", "A cell location", "A chart type", "A formula name"], 2),
            _q("excel", "beginner", "Which function counts numeric cells?", ["COUNT", "COUNTA", "SUM", "NUMBER"], 1),
            _q("excel", "beginner", "Which feature arranges rows based on selected values?", ["Sort", "Freeze", "Merge", "Wrap"], 1),
        ],
        "intermediate": [
            _q("excel", "intermediate", "Which function is commonly used to look up a value in a table?", ["VLOOKUP", "COUNT", "ROUND", "LEN"], 1),
            _q("excel", "intermediate", "Which function returns one value when a condition is true and another when false?", ["IF", "AND", "SUMIF", "MATCH"], 1),
            _q("excel", "intermediate", "What does a PivotTable primarily help with?", ["Summarizing and analyzing data", "Writing Python code", "Creating web pages", "Compressing files"], 1),
            _q("excel", "intermediate", "What does $A$1 represent?", ["A relative reference", "An absolute reference", "A named range", "An error"], 2),
            _q("excel", "intermediate", "Which function sums values that satisfy a condition?", ["SUMIF", "COUNT", "SUM", "TOTALIF"], 1),
        ],
        "advanced": [
            _q("excel", "advanced", "Which pair is commonly used as a flexible alternative to VLOOKUP?", ["INDEX and MATCH", "SUM and COUNT", "LEFT and RIGHT", "ROW and COLUMN only"], 1),
            _q("excel", "advanced", "What is IFERROR useful for?", ["Replacing formula errors with a chosen result", "Sorting values", "Creating a chart", "Deleting worksheets"], 1),
            _q("excel", "advanced", "What does SUMPRODUCT do?", ["Combines multiplication and summation across arrays", "Creates a PivotTable", "Counts text only", "Changes cell colors"], 1),
            _q("excel", "advanced", "Which tool is designed for importing and transforming data?", ["Power Query", "WordArt", "Format Painter", "Goal Seek only"], 1),
            _q("excel", "advanced", "Why use structured table references instead of fixed ranges?", ["They can automatically expand with table data", "They prevent formulas", "They remove headers", "They disable filtering"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # DATA VISUALIZATION
    # ------------------------------------------------------------------
    "data visualization": {
        "beginner": [
            _q("data visualization", "beginner", "Which chart is commonly used to compare categories?", ["Bar chart", "Scatter plot", "Box plot", "Heatmap only"], 1),
            _q("data visualization", "beginner", "Which chart is useful for showing a trend over time?", ["Line chart", "Pie chart", "Tree map", "Radar chart"], 1),
            _q("data visualization", "beginner", "Which chart shows the relationship between two numeric variables?", ["Scatter plot", "Bar chart", "Pie chart", "Gauge"], 1),
            _q("data visualization", "beginner", "What does a legend explain?", ["The meaning of visual encodings", "The database schema", "The source code", "The file size"], 1),
            _q("data visualization", "beginner", "Which chart is commonly used to show parts of a whole?", ["Pie chart", "Scatter plot", "Histogram", "Box plot"], 1),
        ],
        "intermediate": [
            _q("data visualization", "intermediate", "A scatter plot is most useful for exploring what?", ["Relationships between variables", "Only category names", "File formats", "Text grammar"], 1),
            _q("data visualization", "intermediate", "Which chart is best for showing the distribution of a numeric variable?", ["Histogram", "Pie chart", "Bar chart only", "Area map"], 1),
            _q("data visualization", "intermediate", "Why is consistent color encoding important?", ["It helps viewers interpret categories consistently", "It increases database speed", "It removes missing values", "It changes the data type"], 1),
            _q("data visualization", "intermediate", "Which chart helps show median and spread with potential outliers?", ["Box plot", "Pie chart", "Donut chart", "Gauge"], 1),
            _q("data visualization", "intermediate", "What is a dashboard?", ["A coordinated set of visual views for monitoring or analysis", "A database engine", "A Python package only", "A spreadsheet formula"], 1),
        ],
        "advanced": [
            _q("data visualization", "advanced", "What can a dual-axis chart sometimes make harder to interpret?", ["Comparability between differently scaled series", "The file name", "The table headers", "The chart title only"], 1),
            _q("data visualization", "advanced", "What is aggregation bias in visualization?", ["Patterns can differ when data is summarized at a higher level", "A chart has too many colors", "A dataset has no rows", "A legend is missing"], 1),
            _q("data visualization", "advanced", "When can a logarithmic axis be useful?", ["When values span several orders of magnitude", "Only for text", "Only for categories", "Never"], 1),
            _q("data visualization", "advanced", "What are small multiples?", ["Repeated similar charts split by category or condition", "Tiny chart icons", "Compressed images", "Nested databases"], 1),
            _q("data visualization", "advanced", "Why should color palettes consider accessibility?", ["Some users may have difficulty distinguishing certain colors", "It increases SQL speed", "It changes chart values", "It guarantees causation"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # STATISTICS
    # ------------------------------------------------------------------
    "statistics": {
        "beginner": [
            _q("statistics", "beginner", "What is the mean of 2, 4 and 6?", ["3", "4", "5", "6"], 2),
            _q("statistics", "beginner", "Which measure is the middle value of an ordered dataset?", ["Mean", "Mode", "Median", "Range"], 3),
            _q("statistics", "beginner", "Which measure identifies the most frequent value?", ["Mode", "Median", "Mean", "Variance"], 1),
            _q("statistics", "beginner", "What is the range of 3, 5 and 10?", ["5", "7", "8", "10"], 2),
            _q("statistics", "beginner", "What is the probability of a certain event?", ["0", "0.5", "1", "2"], 3),
        ],
        "intermediate": [
            _q("statistics", "intermediate", "What does standard deviation measure?", ["Typical spread around the mean", "The number of variables", "The sample size only", "The median value"], 1),
            _q("statistics", "intermediate", "What does correlation tell us?", ["Association between variables", "Definite causation", "Sample size only", "Whether data is sorted"], 1),
            _q("statistics", "intermediate", "What is the sample mean used to estimate?", ["The population mean", "The population size", "The minimum value only", "The mode only"], 1),
            _q("statistics", "intermediate", "What distribution is symmetric and bell-shaped?", ["Normal distribution", "Uniform only", "Poisson only", "Exponential only"], 1),
            _q("statistics", "intermediate", "What does a confidence interval provide?", ["A range of plausible values for a population parameter", "A guaranteed exact value", "A causal effect", "A list of outliers"], 1),
        ],
        "advanced": [
            _q("statistics", "advanced", "What does a small p-value usually indicate in a hypothesis test?", ["Evidence against the null hypothesis", "Proof the alternative is true", "A large sample size only", "No relationship exists"], 1),
            _q("statistics", "advanced", "What is a Type I error?", ["Rejecting a true null hypothesis", "Failing to reject a false null hypothesis", "Using the wrong chart", "Increasing sample size"], 1),
            _q("statistics", "advanced", "In linear regression, what does a slope coefficient represent?", ["Expected change in the response for a one-unit predictor change, holding other included predictors fixed", "The sample size", "The median residual", "The p-value"], 1),
            _q("statistics", "advanced", "What is the Central Limit Theorem commonly used to justify?", ["Approximate normality of the sampling distribution of the mean under suitable conditions", "All datasets being normal", "Zero variance", "Perfect correlation"], 1),
            _q("statistics", "advanced", "Which measure is generally more resistant to extreme outliers?", ["Median", "Mean", "Variance", "Standard deviation"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # HTML
    # ------------------------------------------------------------------
    "html": {
        "beginner": [
            _q("html", "beginner", "Which HTML tag creates a hyperlink?", ["<link>", "<a>", "<href>", "<url>"], 2),
            _q("html", "beginner", "Which tag creates the largest standard heading?", ["<h6>", "<heading>", "<h1>", "<head>"], 3),
            _q("html", "beginner", "Which tag is used for a paragraph?", ["<p>", "<para>", "<text>", "<pg>"], 1),
            _q("html", "beginner", "Which tag displays an image?", ["<img>", "<image>", "<pic>", "<src>"], 1),
            _q("html", "beginner", "Which element is commonly used to collect user input?", ["<form>", "<inputbox>", "<collect>", "<data>"], 1),
        ],
        "intermediate": [
            _q("html", "intermediate", "Which HTML element is semantic for the main navigation links?", ["<nav>", "<navigate>", "<menuitem>", "<links>"], 1),
            _q("html", "intermediate", "What is the main purpose of the id attribute?", ["Uniquely identify an element", "Apply multiple values", "Create a database", "Resize an image"], 1),
            _q("html", "intermediate", "Which input type is intended for an email address?", ["email", "mailbox", "text-email", "address"], 1),
            _q("html", "intermediate", "Which element groups header cells in a table?", ["<thead>", "<thgroup>", "<headrow>", "<header>"], 1),
            _q("html", "intermediate", "What does the class attribute commonly provide?", ["A reusable hook for styling or scripting", "A unique database key", "A URL", "A page title"], 1),
        ],
        "advanced": [
            _q("html", "advanced", "Which attribute connects a <label> to an input's id?", ["for", "target", "bind", "name"], 1),
            _q("html", "advanced", "Which meta tag helps browsers render responsive layouts on mobile devices?", ["viewport", "responsive", "mobile", "scale"], 1),
            _q("html", "advanced", "What are data-* attributes used for?", ["Storing custom data on elements for scripts", "Loading CSS files only", "Creating SQL tables", "Setting server passwords"], 1),
            _q("html", "advanced", "Why are semantic elements useful?", ["They provide structure and meaning to content", "They automatically encrypt data", "They replace JavaScript", "They remove all CSS"], 1),
            _q("html", "advanced", "Which built-in browser feature can validate required form fields?", ["HTML form validation", "SQL validation", "CSS grid", "SVG only"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # CSS
    # ------------------------------------------------------------------
    "css": {
        "beginner": [
            _q("css", "beginner", "Which CSS property changes text color?", ["font-color", "text-color", "color", "foreground"], 3),
            _q("css", "beginner", "Which symbol selects an element by id?", [".", "#", "*", "&"], 2),
            _q("css", "beginner", "Which symbol selects a class?", ["#", ".", "@", "$"], 2),
            _q("css", "beginner", "Which property adds space outside an element's border?", ["padding", "margin", "gap", "inset"], 2),
            _q("css", "beginner", "Which property controls how an element participates in layout?", ["display", "layout", "positioning", "flow-only"], 1),
        ],
        "intermediate": [
            _q("css", "intermediate", "Which layout system is commonly used for one-dimensional row or column layouts?", ["Flexbox", "Floatbox", "Table only", "Inline only"], 1),
            _q("css", "intermediate", "Which layout system is designed for two-dimensional rows and columns?", ["CSS Grid", "Flexbox only", "Inline-block", "Position absolute"], 1),
            _q("css", "intermediate", "Which rule generally has higher specificity?", ["An id selector", "A type selector", "A universal selector", "A plain element name"], 1),
            _q("css", "intermediate", "Which feature applies styles based on screen conditions?", ["Media queries", "CSS variables", "Transforms", "Keyframes only"], 1),
            _q("css", "intermediate", "What does position: relative allow?", ["Positioning an element relative to its normal position", "Making it fixed to the viewport", "Removing it from layout always", "Turning it into a grid"], 1),
        ],
        "advanced": [
            _q("css", "advanced", "What does box-sizing: border-box change?", ["Width and height include padding and border", "Borders disappear", "Margins are removed", "Elements become inline"], 1),
            _q("css", "advanced", "What can z-index control?", ["Stacking order in overlapping contexts", "Font family", "Grid columns", "Text alignment"], 1),
            _q("css", "advanced", "What are CSS custom properties mainly used for?", ["Reusable variables such as colors or spacing", "Database connections", "HTML parsing", "Image compression"], 1),
            _q("css", "advanced", "What does a pseudo-element such as ::before create?", ["A generated child-like box for styling", "A new HTML document", "A server route", "A JavaScript promise"], 1),
            _q("css", "advanced", "Which function can help create fluid responsive font sizes?", ["clamp()", "scaleText()", "fluid()", "fitfont()"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # JAVASCRIPT
    # ------------------------------------------------------------------
    "javascript": {
        "beginner": [
            _q("javascript", "beginner", "Which keyword declares a block-scoped variable that can be reassigned?", ["let", "const", "varlet", "define"], 1),
            _q("javascript", "beginner", "Which operator checks strict equality?", ["=", "==", "===", "!=="], 3),
            _q("javascript", "beginner", "Which array method adds an item to the end?", ["push()", "add()", "append()", "insertEnd()"], 1),
            _q("javascript", "beginner", "Which function writes a message to the developer console?", ["console.log()", "print()", "log.console()", "echo()"], 1),
            _q("javascript", "beginner", "Which syntax creates a JavaScript object literal?", ["{name: 'Sam'}", "[name: 'Sam']", "(name = 'Sam')", "<name>Sam</name>"], 1),
        ],
        "intermediate": [
            _q("javascript", "intermediate", "What does Array.map() return?", ["A new array containing transformed elements", "A single number only", "A string only", "Nothing"], 1),
            _q("javascript", "intermediate", "What does async/await help with?", ["Writing asynchronous code in a readable style", "Creating CSS classes", "Declaring HTML elements", "Sorting arrays automatically"], 1),
            _q("javascript", "intermediate", "What is a closure?", ["A function retaining access to variables from its lexical scope", "A closed browser tab", "A CSS property", "A loop condition"], 1),
            _q("javascript", "intermediate", "What is destructuring used for?", ["Extracting values from arrays or objects into variables", "Compiling TypeScript", "Sending HTTP requests automatically", "Changing HTML tags"], 1),
            _q("javascript", "intermediate", "What is event bubbling?", ["An event propagating from a target toward ancestor elements", "A network retry", "A promise rejection", "A CSS animation"], 1),
        ],
        "advanced": [
            _q("javascript", "advanced", "What does Promise.all() do?", ["Waits for multiple promises and fulfills when all fulfill", "Runs one promise only", "Cancels every promise", "Turns promises into callbacks"], 1),
            _q("javascript", "advanced", "What is the event loop mainly responsible for?", ["Coordinating asynchronous callbacks with the call stack", "Parsing CSS", "Compiling HTML", "Managing SQL indexes"], 1),
            _q("javascript", "advanced", "What is a key difference between var and let regarding hoisting?", ["let is in a temporal dead zone before initialization", "var cannot be reassigned", "let is function-scoped only", "There is no difference"], 1),
            _q("javascript", "advanced", "Why is debouncing useful for search input?", ["It reduces the number of rapid calls by waiting for a pause", "It sorts results", "It encrypts requests", "It caches every keystroke permanently"], 1),
            _q("javascript", "advanced", "What does immutability mean in state management?", ["Creating new values instead of mutating existing state directly", "Never creating objects", "Using only strings", "Making variables global"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # REACT
    # ------------------------------------------------------------------
    "react": {
        "beginner": [
            _q("react", "beginner", "What is a React component commonly represented by?", ["A JavaScript function or class", "A SQL table", "A CSS selector", "A JSON file only"], 1),
            _q("react", "beginner", "Which hook is used to store local component state?", ["useState", "useStore", "useData", "useValue"], 1),
            _q("react", "beginner", "How are values usually passed from a parent to a child component?", ["Props", "SQL", "Selectors", "Routes only"], 1),
            _q("react", "beginner", "Which syntax is commonly used to render a list from an array?", ["array.map(...) in JSX", "forSQL", "foreachHTML", "renderArrayOnly"], 1),
            _q("react", "beginner", "What is JSX?", ["A syntax extension that lets you write markup-like code in JavaScript", "A database query language", "A CSS preprocessor", "A browser plugin"], 1),
        ],
        "intermediate": [
            _q("react", "intermediate", "Which hook runs side effects after rendering?", ["useEffect", "useRender", "useAsyncOnly", "useSide"], 1),
            _q("react", "intermediate", "Why does React ask for a key when rendering lists?", ["To help identify list items across renders", "To encrypt list data", "To style items", "To sort them"], 1),
            _q("react", "intermediate", "What is a controlled input?", ["An input whose value is driven by React state", "An input controlled by CSS", "An input with no events", "An input only inside a form"], 1),
            _q("react", "intermediate", "What does lifting state up mean?", ["Moving shared state to the nearest common parent", "Moving state to the server", "Deleting local state", "Creating a new hook"], 1),
            _q("react", "intermediate", "How can a component conditionally render content?", ["Using JavaScript conditions such as ternaries or &&", "Only with CSS", "Only with SQL", "Only with a router"], 1),
        ],
        "advanced": [
            _q("react", "advanced", "What is React.memo mainly used for?", ["Avoiding unnecessary re-renders when props have not changed", "Fetching APIs", "Creating CSS", "Managing SQL"], 1),
            _q("react", "advanced", "What is a custom hook?", ["A reusable function that uses React hooks and related logic", "A browser extension", "A CSS class", "A server route"], 1),
            _q("react", "advanced", "Why is the dependency array in useEffect important?", ["It controls when the effect is re-run", "It creates component props", "It styles the page", "It stores database rows"], 1),
            _q("react", "advanced", "Why should React state usually be updated immutably?", ["It makes changes predictable and supports efficient rendering patterns", "It makes JavaScript faster in every case", "It prevents components", "It removes props"], 1),
            _q("react", "advanced", "What is reconciliation in React?", ["Comparing the new and previous UI representations to determine updates", "Compiling CSS", "Running SQL transactions", "Calling an API"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # DATABASES
    # ------------------------------------------------------------------
    "databases": {
        "beginner": [
            _q("databases", "beginner", "What is a primary key used for?", ["Uniquely identifying records", "Storing duplicate rows", "Deleting a database", "Formatting tables"], 1),
            _q("databases", "beginner", "What does a foreign key represent?", ["A relationship to a key in another table", "A password", "A duplicate column", "A backup file"], 1),
            _q("databases", "beginner", "In a relational table, what is a row?", ["A record", "A database", "A query", "A constraint"], 1),
            _q("databases", "beginner", "Why is normalization used?", ["To reduce unnecessary redundancy", "To increase duplicate values", "To format text", "To replace SQL"], 1),
            _q("databases", "beginner", "What is a relational database?", ["A database that organizes related data in tables", "A file compressor", "A web browser", "A programming language"], 1),
        ],
        "intermediate": [
            _q("databases", "intermediate", "What does third normal form mainly aim to remove?", ["Transitive dependencies", "All primary keys", "All indexes", "All foreign keys"], 1),
            _q("databases", "intermediate", "What is an index mainly used for?", ["Improving lookup performance for suitable queries", "Replacing tables", "Removing constraints", "Backing up data"], 1),
            _q("databases", "intermediate", "Which property means a transaction's changes are treated as a single unit?", ["Atomicity", "Isolation", "Durability", "Consistency only"], 1),
            _q("databases", "intermediate", "What is a transaction?", ["A logical unit of database work", "A table row", "An index page", "A column type"], 1),
            _q("databases", "intermediate", "A one-to-many relationship usually means what?", ["One record in one table can relate to many in another", "Every row must be unique across all tables", "There are no keys", "Only one table exists"], 1),
        ],
        "advanced": [
            _q("databases", "advanced", "What is a composite index?", ["An index built from multiple columns", "An index on multiple databases", "A backup index", "A temporary table"], 1),
            _q("databases", "advanced", "Why can too many indexes hurt write performance?", ["Indexes must also be maintained during inserts and updates", "Indexes delete data", "Indexes prevent reads", "Indexes remove transactions"], 1),
            _q("databases", "advanced", "What is a transaction isolation level used to control?", ["How concurrent transactions can observe each other's changes", "Column names", "Table colors", "Backup file names"], 1),
            _q("databases", "advanced", "Why might a designer intentionally denormalize data?", ["To improve read performance for a known workload", "To eliminate all keys", "To prevent queries", "To remove constraints"], 1),
            _q("databases", "advanced", "What is a deadlock?", ["Two or more transactions wait on resources held by each other", "A deleted table", "A broken index file", "An empty database"], 1),
        ],
    },

    # ------------------------------------------------------------------
    # MACHINE LEARNING
    # ------------------------------------------------------------------
    "machine learning": {
        "beginner": [
            _q("machine learning", "beginner", "Which type of learning uses labelled training data?", ["Unsupervised Learning", "Supervised Learning", "Reinforcement Learning", "Random Learning"], 2),
            _q("machine learning", "beginner", "Which task predicts a category such as spam or not spam?", ["Classification", "Regression", "Clustering only", "Compression"], 1),
            _q("machine learning", "beginner", "Which task predicts a numeric value such as house price?", ["Regression", "Classification", "Clustering", "Ranking only"], 1),
            _q("machine learning", "beginner", "Why split data into train and test sets?", ["To evaluate generalization on unseen data", "To increase labels", "To remove all noise", "To avoid preprocessing"], 1),
            _q("machine learning", "beginner", "What is overfitting?", ["Learning the training data too closely and performing poorly on new data", "Using too little data only", "Having no features", "Using a test set"], 1),
        ],
        "intermediate": [
            _q("machine learning", "intermediate", "What does precision measure?", ["The fraction of predicted positives that are actually positive", "The fraction of all positives found", "The total number of samples", "The training time"], 1),
            _q("machine learning", "intermediate", "What does recall measure?", ["The fraction of actual positives that are correctly identified", "The fraction of predicted negatives", "The number of features", "The model size"], 1),
            _q("machine learning", "intermediate", "Why is feature scaling useful for some algorithms?", ["It puts numeric features on comparable scales", "It creates labels", "It removes all outliers", "It guarantees accuracy"], 1),
            _q("machine learning", "intermediate", "What is cross-validation used for?", ["Estimating model performance across multiple train/validation splits", "Replacing the test set permanently", "Creating charts", "Collecting labels"], 1),
            _q("machine learning", "intermediate", "What does regularization help reduce?", ["Overfitting", "Dataset size", "Number of classes", "Missing values automatically"], 1),
        ],
        "advanced": [
            _q("machine learning", "advanced", "What is data leakage?", ["Using information during training that would not be available at prediction time", "Having too many rows", "Missing labels only", "A slow database"], 1),
            _q("machine learning", "advanced", "Why can class imbalance make accuracy misleading?", ["A majority class can dominate the accuracy value", "Accuracy becomes negative", "Features disappear", "The model cannot train"], 1),
            _q("machine learning", "advanced", "What does ROC-AUC summarize?", ["Ranking performance across classification thresholds", "Regression error only", "Training time", "Number of features"], 1),
            _q("machine learning", "advanced", "What is hyperparameter tuning?", ["Searching for good settings that control model training", "Changing labels after prediction", "Cleaning a database", "Plotting the confusion matrix"], 1),
            _q("machine learning", "advanced", "What is the bias-variance trade-off about?", ["Balancing underfitting and sensitivity to training data", "Choosing a database index", "Reducing file size", "Selecting a chart type"], 1),
        ],
    },
}


# ------------------------------------------------------------------
## ECE-specific question bank. Insert this block before the EXPERT QUESTION BANK section.
# Each difficulty has three questions per skill; Python reuses the existing Python bank.
_ECE_ITEMS = {
    "c programming": {
        "beginner": [
            ("Which header declares printf() in C?", ["stdio.h", "stdlib.h", "string.h", "math.h"], 1),
            ("Which format specifier is commonly used to print an int?", ["%c", "%d", "%s", "%f"], 2),
            ("Array indexing in C starts at which value?", ["-1", "0", "1", "Depends on array size"], 2),
        ],
        "intermediate": [
            ("What does a pointer store?", ["A memory address", "Only a character", "A loop count", "A file name"], 1),
            ("Which operator accesses a structure member through a pointer?", [".", "->", "::", "&"], 2),
            ("Which function allocates a block of memory dynamically?", ["printf()", "scanf()", "malloc()", "strlen()"], 3),
        ],
        "advanced": [
            ("What is undefined behavior in C?", ["Behavior the C standard does not define", "A compiler warning only", "A required runtime message", "A type of comment"], 1),
            ("What can happen when allocated memory is never freed and is no longer reachable?", ["A memory leak", "A syntax error", "An automatic reset", "A linker rename"], 1),
            ("What does the static storage duration of a local variable generally mean?", ["It retains its value between function calls", "It is recreated on every call", "It is always stored in a CPU register", "It can only hold strings"], 1),
        ],
    },
    "circuit analysis": {
        "beginner": [
            ("Ohm's law relates voltage to which product?", ["Current times resistance", "Current divided by resistance", "Resistance minus current", "Power divided by time"], 1),
            ("Two resistors in series have what equivalent resistance?", ["The sum of their resistances", "The smaller resistance only", "Always zero", "The product only"], 1),
            ("The SI unit of electric current is the:", ["Volt", "Ohm", "Ampere", "Watt"], 3),
        ],
        "intermediate": [
            ("Kirchhoff's Current Law follows from conservation of:", ["Electric charge", "Magnetic flux only", "Resistance", "Frequency"], 1),
            ("For an ideal voltage divider with two series resistors, the output across the lower resistor is:", ["Vin times Rlower divided by total resistance", "Always Vin", "Always zero", "Vin times total resistance"], 1),
            ("The capacitive reactance of an ideal capacitor decreases when frequency:", ["Increases", "Decreases", "Becomes zero only", "Has no effect"], 1),
        ],
        "advanced": [
            ("Thevenin's theorem replaces a linear two-terminal network with:", ["An equivalent voltage source and series resistance", "A current source only with no resistance", "A capacitor only", "An ideal transformer in every case"], 1),
            ("The time constant of a simple series RC circuit is:", ["R divided by C", "R times C", "C divided by R", "R plus C"], 2),
            ("In sinusoidal steady-state analysis, impedance is used to represent:", ["Opposition to AC including phase effects", "Only physical wire length", "Only DC current", "Power factor alone"], 1),
        ],
    },
    "digital electronics": {
        "beginner": [
            ("An AND gate outputs 1 when:", ["All inputs are 1", "Any input is 1", "All inputs are 0", "Inputs differ"], 1),
            ("The binary number 10 represents which decimal value?", ["1", "2", "10", "4"], 2),
            ("A flip-flop is commonly used to store:", ["One bit", "One byte only", "An analog waveform", "A resistor value"], 1),
        ],
        "intermediate": [
            ("A multiplexer selects:", ["One of several inputs for a single output", "One clock for every circuit", "An analog resistance", "Only a power supply"], 1),
            ("An XOR gate outputs 1 when its two inputs are:", ["Different", "Both 0 only", "Both 1 only", "Always equal"], 1),
            ("Karnaugh maps are mainly used to:", ["Simplify Boolean expressions", "Measure current", "Generate clock frequency", "Store program memory"], 1),
        ],
        "advanced": [
            ("Setup time is the minimum time data must be stable:", ["Before the active clock edge", "After power is removed", "Only during reset", "After compilation"], 1),
            ("A finite-state machine consists primarily of states and:", ["Transitions based on inputs", "Resistors and capacitors only", "Database tables", "Analog filters only"], 1),
            ("A synchronous counter changes state in coordination with:", ["A clock signal", "A random noise source", "Output voltage only", "The board temperature only"], 1),
        ],
    },
    "analog electronics": {
        "beginner": [
            ("A diode ideally allows current to flow mainly in:", ["One direction", "Both directions equally", "No direction under any condition", "Only through its case"], 1),
            ("A BJT used as a switch is commonly driven between cutoff and:", ["Saturation", "Resonance", "Breakdown always", "Open-loop gain"], 1),
            ("For an ideal op-amp, the input current is approximately:", ["Zero", "Infinite", "Equal to output current", "Always 1 ampere"], 1),
        ],
        "intermediate": [
            ("The magnitude of the gain of an ideal inverting op-amp circuit is:", ["Rf divided by Rin", "Rin divided by Rf only with positive sign", "Always 1", "The supply voltage"], 1),
            ("A rectifier converts AC into:", ["Pulsating DC", "Pure sine-wave AC at twice voltage", "Only digital data", "Resistance"], 1),
            ("A common-emitter BJT amplifier typically provides:", ["Voltage gain with phase inversion", "No current or voltage gain in any case", "Only optical output", "A purely digital clock"], 1),
        ],
        "advanced": [
            ("Negative feedback in an amplifier generally improves:", ["Gain stability and linearity", "Distortion in every case", "Sensitivity to component variation", "Output power without limits"], 1),
            ("An op-amp's slew rate limits the maximum rate of change of its:", ["Output voltage", "Input resistance only", "Package mass", "DC supply polarity"], 1),
            ("A differential amplifier responds primarily to the:", ["Difference between its two input signals", "Sum of supply voltages only", "Temperature of a PCB trace", "Absolute value of one resistor"], 1),
        ],
    },
    "signals and systems": {
        "beginner": [
            ("The frequency of a periodic signal is measured in:", ["Hertz", "Ohms", "Coulombs", "Webers"], 1),
            ("A sinusoidal signal is described by amplitude, frequency and:", ["Phase", "Resistance only", "Bit depth only", "Inductance only"], 1),
            ("An impulse signal is often used to study a system's:", ["Impulse response", "PCB color", "Supply connector", "Source-code length"], 1),
        ],
        "intermediate": [
            ("Convolution is used in LTI systems to find output from input and:", ["Impulse response", "Resistor color code", "Clock pin number only", "Battery capacity"], 1),
            ("The Nyquist sampling condition requires a sampling rate greater than twice the:", ["Highest signal frequency", "Signal amplitude", "DC offset", "Number of channels"], 1),
            ("A system is time-invariant when a time shift at its input produces:", ["The same time shift at its output", "A different system every time", "Zero output always", "Only a frequency doubling"], 1),
        ],
        "advanced": [
            ("For an LTI system, the Fourier transform of the output is the product of input spectrum and:", ["System frequency response", "Input amplitude squared always", "Sampling interval only", "Resistance value"], 1),
            ("A causal discrete-time system's impulse response is zero for:", ["Negative time indices", "All positive indices", "The zero index only", "Every index"], 1),
            ("A band-limited signal can be reconstructed from ideal samples when sampled above its:", ["Nyquist rate", "DC level", "Peak amplitude", "Phase offset"], 1),
        ],
    },
    "communication systems": {
        "beginner": [
            ("Modulation changes a carrier's property according to the:", ["Information signal", "PCB solder mask", "Resistor color", "Program variable name"], 1),
            ("AM stands for:", ["Amplitude Modulation", "Analog Memory", "Automatic Matching", "Average Measurement"], 1),
            ("Bandwidth is a measure of a signal's frequency:", ["Range", "Voltage only", "Cable weight", "Bit order"], 1),
        ],
        "intermediate": [
            ("For conventional AM, the modulation index indicates the relative:", ["Amplitude of the modulating signal", "Length of the antenna only", "Resistance of the receiver", "Number of batteries"], 1),
            ("Increasing signal-to-noise ratio generally improves reception quality because noise is:", ["Smaller relative to the signal", "Always eliminated completely", "Converted to bandwidth", "Required to exceed the signal"], 1),
            ("A basic digital communication receiver makes decisions about transmitted:", ["Symbols or bits", "PCB layer colors", "Resistor packages", "Source-code indentation"], 1),
        ],
        "advanced": [
            ("QAM conveys information by varying both amplitude and:", ["Phase", "Wire color", "DC resistance only", "Antenna height only"], 1),
            ("A matched filter is designed to maximize output SNR for a known signal in:", ["Additive white Gaussian noise", "A noiseless circuit only", "A purely mechanical system", "An unpowered circuit"], 1),
            ("Bit error rate is the ratio of incorrectly received bits to:", ["Total received bits", "Carrier frequency", "Antenna length", "Modulation amplitude"], 1),
        ],
    },
    "microcontrollers": {
        "beginner": [
            ("A GPIO pin is commonly configured as an input or:", ["Output", "Database", "Compiler", "Frequency unit"], 1),
            ("A timer peripheral can be used to measure time intervals or generate:", ["Periodic events", "PCB artwork", "Source-code comments", "A chemical signal"], 1),
            ("An interrupt lets a processor respond to an event without:", ["Continuously polling it", "Running any instructions ever", "Using memory", "Having a clock"], 1),
        ],
        "intermediate": [
            ("An ADC converts an analog input into a:", ["Digital representation", "Higher resistance automatically", "Clock crystal", "PCB layer"], 1),
            ("UART communication commonly uses TX and:", ["RX", "VCC only", "SCL only", "MISO only"], 1),
            ("PWM controls average delivered power by varying the signal's:", ["Duty cycle", "File extension", "Pin label font", "Compiler version"], 1),
        ],
        "advanced": [
            ("DMA transfers data between peripherals and memory with reduced:", ["CPU involvement", "Clock frequency in every case", "Memory capacity", "Need for data integrity"], 1),
            ("A watchdog timer helps recover when software:", ["Stops servicing it due to a fault", "Runs perfectly", "Prints a message", "Changes a variable name"], 1),
            ("I2C devices share SDA and SCL; SCL is the:", ["Serial clock line", "Analog output line", "Reset-only line", "Power return only"], 1),
        ],
    },
    "embedded systems": {
        "beginner": [
            ("Firmware is software designed to run on:", ["A hardware device or embedded system", "Only a spreadsheet", "A PCB solder mask", "A resistor"], 1),
            ("A real-time system must meet required:", ["Timing deadlines", "Screen resolution only", "File naming rules only", "Internet speed in every case"], 1),
            ("Memory-mapped I/O lets software access device registers through:", ["Addresses in the processor's address space", "Only printed labels", "A spreadsheet formula", "A web URL"], 1),
        ],
        "intermediate": [
            ("An interrupt service routine should generally be kept short to reduce:", ["Interrupt latency for other work", "The number of CPU instructions to zero", "Memory size permanently", "The clock's physical size"], 1),
            ("A hard real-time deadline miss can be considered:", ["A system failure", "Always harmless", "A syntax highlight", "A PCB color change"], 1),
            ("An RTOS scheduler decides which ready task should:", ["Run next", "Be soldered next", "Change its binary format", "Replace the processor"], 1),
        ],
        "advanced": [
            ("Priority inversion occurs when a high-priority task is blocked by a lower-priority task holding a:", ["Needed resource or lock", "Higher clock frequency", "PCB layer", "Compiler warning"], 1),
            ("A bootloader commonly supports loading or updating:", ["Firmware", "Resistor values automatically", "Circuit diagrams only", "Antenna radiation patterns"], 1),
            ("A race condition can occur when behavior depends on the timing of:", ["Concurrent operations", "The PCB's printed text", "A static logo", "An offline PDF"], 1),
        ],
    },
    "vlsi basics": {
        "beginner": [
            ("CMOS logic commonly uses complementary:", ["NMOS and PMOS transistors", "Inductors only", "Mechanical switches only", "Optical fibers"], 1),
            ("A CMOS inverter produces an output opposite to its:", ["Input logic level", "Supply label", "Package size", "Clock frequency in all cases"], 1),
            ("VLSI stands for very-large-scale:", ["Integration", "Inductance", "Interference", "Insulation"], 1),
        ],
        "intermediate": [
            ("Dynamic CMOS power is strongly related to switching activity, capacitance, and:", ["Supply voltage squared and frequency", "PCB color and font", "Only transistor package weight", "The number of comments"], 1),
            ("Setup timing checks whether data arrives sufficiently early before a:", ["Clock edge", "PCB shipment", "Software release note", "Resistor label"], 1),
            ("PVT corners refer to process, voltage, and:", ["Temperature", "Timing diagram color", "Transistor name length", "Test file path"], 1),
        ],
        "advanced": [
            ("Static timing analysis evaluates timing paths without requiring:", ["Applying simulation vectors for every possible input", "A clock definition", "Cell delays", "Path constraints"], 1),
            ("Metastability can occur when setup or hold requirements are violated at a:", ["Flip-flop input", "PCB silkscreen", "Resistor body", "Text editor"], 1),
            ("A clock-domain crossing needs care because the two domains may have:", ["Unrelated clock timing", "Identical phase by definition", "No sequential logic", "Only analog signals"], 1),
        ],
    },
    "matlab": {
        "beginner": [
            ("In MATLAB, the colon expression 1:3 creates:", ["A vector containing 1, 2, 3", "A matrix of all zeros", "A string", "A plot automatically"], 1),
            ("Which MATLAB command is commonly used to plot y against x?", ["plot(x,y)", "draw(x,y)", "chart(x,y)", "graphfile(x,y)"], 1),
            ("In MATLAB, the semicolon at the end of a statement usually suppresses:", ["Command-window output", "The calculation itself", "All variables", "The program file"], 1),
        ],
        "intermediate": [
            ("The operator .* in MATLAB performs:", ["Element-wise multiplication", "Matrix inversion", "Commenting", "Matrix concatenation only"], 1),
            ("For a matrix A, size(A) returns its:", ["Dimensions", "Determinant only", "Largest element only", "File size in bytes"], 1),
            ("Which command creates a regularly spaced time vector from 0 to 1 with 101 points?", ["linspace(0,1,101)", "range(0,1,101)", "time(0,1)", "vector(101)"], 1),
        ],
        "advanced": [
            ("The FFT is commonly used to compute a discrete signal's:", ["Frequency-domain representation", "PCB layout", "Power connector pinout", "Source-code checksum"], 1),
            ("Why is vectorized MATLAB code often preferred over explicit loops for array operations?", ["It can use optimized array operations and reduce interpreter overhead", "It guarantees zero memory use", "It disables numerical rounding", "It removes the need to understand dimensions"], 1),
            ("Ill-conditioned linear systems can cause small input errors to produce:", ["Large solution errors", "Guaranteed exact answers", "A change in programming language", "No numerical effect"], 1),
        ],
    },
    "pcb design": {
        "beginner": [
            ("PCB silkscreen is mainly used for:", ["Component labels and board markings", "Carrying all high-speed signals", "Replacing copper traces", "Storing firmware"], 1),
            ("A copper trace on a PCB provides an electrical:", ["Connection", "Software function", "Clock instruction", "Material test report"], 1),
            ("A ground plane can provide a low-impedance return path and help reduce:", ["Noise and interference", "All component costs to zero", "The need for power", "All thermal effects"], 1),
        ],
        "intermediate": [
            ("A decoupling capacitor placed near an IC supply pin helps provide local charge and reduce:", ["Supply noise", "Program size", "The number of PCB layers automatically", "Connector labels"], 1),
            ("Differential high-speed signals are commonly routed as a pair with controlled:", ["Spacing and impedance", "Silkscreen font only", "Solder-mask color only", "Board serial number"], 1),
            ("A via connects copper features on:", ["Different PCB layers", "Only the same point on one surface", "A source-code file", "A battery chemical cell"], 1),
        ],
        "advanced": [
            ("A continuous reference plane helps high-speed routing by providing a predictable:", ["Return-current path", "Component value", "Firmware checksum", "Antenna protocol"], 1),
            ("Controlled impedance is especially important when PCB trace dimensions affect:", ["High-speed signal reflections", "Silkscreen readability only", "The program's variable names", "The board's filename"], 1),
            ("Thermal relief on a copper plane is designed to make a pad easier to:", ["Solder by reducing heat sinking", "Use as an antenna in every circuit", "Convert into software", "Disconnect from its net"], 1),
        ],
    },
}

ECE_QUESTION_BANK = {
    skill: {
        difficulty: [
            _q(skill, difficulty, question, options, answer)
            for question, options, answer in items
        ]
        for difficulty, items in bands.items()
    }
    for skill, bands in _ECE_ITEMS.items()
}
ECE_QUESTION_BANK["python"] = QUESTION_BANK["python"]
#  EXPERT QUESTION BANK
# Rating 5 is intentionally mapped to questions that test deeper
# concepts, application and reasoning rather than simple definitions.
# ------------------------------------------------------------------
EXPERT_QUESTION_BANK = {
    "python": [
        _q("python", "expert", "In CPython, what is the main effect of the Global Interpreter Lock (GIL) on CPU-bound threads?", ["Only one thread executes Python bytecode at a time", "All threads run on the GPU", "Threads cannot perform I/O", "Every thread gets a separate interpreter automatically"], 1),
        _q("python", "expert", "Which function is appropriate when a nested list must be copied so that inner lists are independent too?", ["copy.copy", "copy.deepcopy", "list.copy only", "tuple"], 2),
        _q("python", "expert", "Which protocol lets an object work with a `with` statement?", ["__iter__ and __next__", "__enter__ and __exit__", "__get__ and __set__", "__call__ and __repr__"], 2),
        _q("python", "expert", "Why can a generator expression use less memory than building an equivalent list?", ["It stores every result twice", "It produces values lazily instead of materializing them all", "It converts values to strings", "It disables iteration"], 2),
        _q("python", "expert", "What does `functools.lru_cache` primarily provide for a function with hashable arguments?", ["Memoization of repeated calls", "Automatic parallel execution", "Database persistence", "Type checking"], 1),
    ],
    "java": [
        _q("java", "expert", "What happens to most generic type information at runtime in Java?", ["It is generally erased due to type erasure", "It is converted to SQL", "It is stored permanently in bytecode metadata for all operations", "It disables inheritance"], 1),
        _q("java", "expert", "Which statement best describes `volatile` in Java?", ["It guarantees atomicity for every operation", "It improves visibility of writes across threads but does not make compound operations atomic", "It makes an object immutable", "It serializes all threads"], 2),
        _q("java", "expert", "Why is overriding `equals()` usually paired with overriding `hashCode()`?", ["Java requires both methods to have identical code", "Equal objects must produce the same hash code for hash-based collections", "hashCode controls inheritance", "equals is only used by the compiler"], 2),
        _q("java", "expert", "What is the main advantage of try-with-resources?", ["It automatically closes resources that implement AutoCloseable", "It retries failed SQL queries", "It converts checked exceptions to unchecked exceptions", "It prevents all runtime exceptions"], 1),
        _q("java", "expert", "What does the Java Memory Model require a correctly synchronized program to provide between threads?", ["Only identical CPU speeds", "Visibility and ordering guarantees through synchronization mechanisms", "Automatic deep copies of all objects", "A separate JVM for each thread"], 2),
    ],
    "sql": [
        _q("sql", "expert", "Which SQL feature calculates values such as running totals while keeping one output row per input row?", ["Window functions", "GROUP BY only", "DISTINCT", "UNION"], 1),
        _q("sql", "expert", "Why can applying a function directly to an indexed column sometimes prevent efficient index use?", ["The database may need to compute the function for many rows instead of using the raw index ordering", "Functions always delete indexes", "Indexes only work on strings", "Functions force a CROSS JOIN"], 1),
        _q("sql", "expert", "For a composite index on `(last_name, first_name)`, which query can generally benefit most directly from the leftmost prefix?", ["Filtering by first_name only", "Filtering by last_name only", "Filtering by an unrelated column", "Sorting by an unrelated column"], 2),
        _q("sql", "expert", "What is the main purpose of a common table expression (CTE) in a complex query?", ["To create a named intermediate result within the statement", "To permanently create a database", "To disable transactions", "To replace all indexes"], 1),
        _q("sql", "expert", "Which isolation issue occurs when a transaction can see new rows inserted by another transaction during a repeated range query?", ["Dirty read", "Non-repeatable read", "Phantom read", "Syntax error"], 3),
    ],
    "excel": [
        _q("excel", "expert", "Which Excel feature is most suitable for building a reusable data-cleaning workflow from imported files?", ["Power Query", "Format Painter", "Freeze Panes", "Goal Seek"], 1),
        _q("excel", "expert", "What is a key advantage of the `LET` function in a complex formula?", ["It can assign names to intermediate calculations and reduce repeated work", "It creates database tables", "It removes all errors automatically", "It disables recalculation"], 1),
        _q("excel", "expert", "Which Excel feature allows formulas such as FILTER to return results that spill into neighboring cells?", ["Dynamic arrays", "Page Layout", "Conditional formatting", "Data validation"], 1),
        _q("excel", "expert", "Why are structured references in Excel Tables useful in larger models?", ["They use table column names and adjust automatically as the table changes", "They prevent formulas from recalculating", "They convert all values to text", "They remove the need for any formulas"], 1),
        _q("excel", "expert", "What is Power Pivot primarily designed to support?", ["Data models, relationships and advanced analysis with DAX", "Drawing shapes", "Editing images", "Changing worksheet themes only"], 1),
    ],
    "data visualization": [
        _q("data visualization", "expert", "A chart shows different trends after data is aggregated by region versus shown at the individual-record level. What issue should you investigate?", ["Aggregation bias", "Font kerning", "Pixel density", "HTML semantics"], 1),
        _q("data visualization", "expert", "When comparing quantities across many categories, which visual encoding is generally easiest to compare accurately?", ["Position on a common scale", "Area of circles", "Decorative icons", "3D perspective"], 1),
        _q("data visualization", "expert", "When is a diverging color scale most appropriate?", ["When values have a meaningful midpoint such as zero", "Whenever all values are positive", "Only for categorical labels", "Only for pie charts"], 1),
        _q("data visualization", "expert", "Why can dual-axis charts be misleading?", ["Changing the two axis scales can visually exaggerate or hide relationships", "They cannot display numeric data", "They always remove legends", "They only work with pie charts"], 1),
        _q("data visualization", "expert", "What is the main idea behind small multiples?", ["Using repeated, consistent mini-charts to compare groups or categories", "Using many unrelated chart types", "Adding 3D effects to one chart", "Removing axes from every plot"], 1),
    ],
    "statistics": [
        _q("statistics", "expert", "If residual variance increases with the fitted value in a linear regression, what issue is suggested?", ["Heteroscedasticity", "Perfect multicollinearity", "Zero variance", "Categorical encoding"], 1),
        _q("statistics", "expert", "What is bootstrap resampling mainly used for?", ["Estimating sampling variability or uncertainty by repeated resampling", "Replacing every missing value", "Guaranteeing normality", "Sorting a dataset"], 1),
        _q("statistics", "expert", "Why is multiple-testing correction used when many hypotheses are tested?", ["To control the chance of false discoveries or family-wise errors", "To increase sample size automatically", "To remove correlation", "To make every p-value equal"], 1),
        _q("statistics", "expert", "In a regression model with an interaction term between X and Z, what does the interaction typically represent?", ["The effect of X changes depending on Z", "X and Z must be identical", "Z is always the dependent variable", "The intercept becomes zero"], 1),
        _q("statistics", "expert", "Which interval is designed to capture the likely value of a single future observation rather than the population mean?", ["Prediction interval", "Confidence interval for the mean", "Standard error only", "Interquartile range"], 1),
    ],
    "html": [
        _q("html", "expert", "Why is a native semantic element often preferable to adding ARIA roles to a generic div?", ["Native semantics usually provide built-in browser and accessibility behavior", "ARIA removes all browser behavior", "div elements load more slowly", "Semantic elements cannot contain text"], 1),
        _q("html", "expert", "When opening an untrusted link in a new tab, which relationship value helps prevent the new page from controlling the opener?", ["noopener", "nofollow-only", "stylesheet", "preload"], 1),
        _q("html", "expert", "What is the main purpose of the `<template>` element?", ["To hold inert markup that can later be cloned and inserted into the document", "To submit forms automatically", "To execute SQL", "To replace CSS"], 1),
        _q("html", "expert", "Which combination correctly associates a label with an input for accessibility?", ["The label's `for` matches the input's `id`", "The label's `name` matches the input's `class`", "The input's `href` matches the label's `src`", "The label must always be inside a button"], 1),
        _q("html", "expert", "Which attribute can provide a regular-expression constraint for many text-like form inputs?", ["pattern", "regex", "validate", "constraint"], 1),
    ],
    "css": [
        _q("css", "expert", "Which CSS property can create a new stacking context and limit how descendants participate in stacking and painting?", ["contain", "font-style", "letter-spacing", "text-align"], 1),
        _q("css", "expert", "Why can `minmax(0, 1fr)` be useful in a CSS Grid column?", ["It lets the track shrink to zero instead of being forced by min-content size", "It disables grid layout", "It makes the column fixed at 1px", "It converts the grid to flexbox"], 1),
        _q("css", "expert", "What is the purpose of `clamp(min, preferred, max)`?", ["It keeps a computed value within a lower and upper bound", "It disables media queries", "It creates only fixed-size fonts", "It selects DOM elements"], 1),
        _q("css", "expert", "What is a key advantage of CSS custom properties such as `--accent`?", ["They can store reusable values and participate in the cascade and inheritance", "They are only valid in JavaScript", "They permanently change HTML", "They cannot be overridden"], 1),
        _q("css", "expert", "Why can `transform` unexpectedly affect the positioning of descendants?", ["It can establish a containing/stacking context that changes how descendants are rendered", "Transforms remove all descendants", "Transforms disable z-index globally", "Transform only changes text color"], 1),
    ],
    "javascript": [
        _q("javascript", "expert", "After the current call stack finishes, which queued work is generally processed before the next task such as a timer callback?", ["Microtasks such as resolved Promise callbacks", "All timers first", "Only animation frames", "CSS transitions only"], 1),
        _q("javascript", "expert", "What is event delegation mainly based on?", ["Handling events on a common ancestor and using bubbling to determine the target", "Creating one listener for every possible future element", "Disabling event bubbling", "Using only capture events"], 1),
        _q("javascript", "expert", "What does `AbortController` commonly allow when used with `fetch()`?", ["Cancelling an in-flight request", "Compiling JavaScript", "Changing HTTP methods after completion", "Blocking all browser events"], 1),
        _q("javascript", "expert", "Why can an asynchronous callback sometimes observe stale state in a closure?", ["The callback captured values from an earlier render or execution context", "Closures always delete variables", "Promises copy the DOM", "JavaScript disables mutation"], 1),
        _q("javascript", "expert", "What is a common use of `WeakMap`?", ["Associating metadata with objects without preventing those objects from being garbage-collected", "Storing primitive keys permanently", "Sorting arrays automatically", "Serializing JSON"], 1),
    ],
    "react": [
        _q("react", "expert", "Why should `useMemo` usually be treated as a performance optimization rather than a correctness requirement?", ["React may discard the memoized value and recompute it", "useMemo guarantees persistence across page reloads", "useMemo replaces state", "useMemo prevents all re-renders"], 1),
        _q("react", "expert", "What can happen when a component's effect closes over an old state value and its dependencies are incorrect?", ["The effect can use stale data", "The component automatically unmounts", "React converts state to props", "The browser blocks JavaScript"], 1),
        _q("react", "expert", "When is `useReducer` often a good choice?", ["When state transitions are complex or involve related updates", "Only when rendering plain text", "Only for CSS", "When the app has no state"], 1),
        _q("react", "expert", "Why are React state updates usually treated immutably?", ["It helps React detect changes predictably and avoids unintended mutation of existing state", "Mutation is forbidden by JavaScript", "Immutable state is stored in SQL", "React cannot use objects"], 1),
        _q("react", "expert", "What does React reconciliation broadly describe?", ["Comparing a new element tree with the previous one to determine updates to the rendered UI", "Sending SQL queries", "Compiling CSS", "Creating browser tabs"], 1),
    ],
    "databases": [
        _q("databases", "expert", "What is the main purpose of database normalization?", ["Reducing unnecessary redundancy and update anomalies", "Making every query slower", "Eliminating all indexes", "Forcing every table to have one row"], 1),
        _q("databases", "expert", "What is the key goal of serializability in transaction processing?", ["The concurrent result should be equivalent to some serial execution", "Every transaction must run on a separate server", "All transactions must be read-only", "Every query must use an index"], 1),
        _q("databases", "expert", "What is MVCC primarily used for?", ["Allowing multiple transaction versions so readers and writers can often proceed with less blocking", "Compressing images", "Replacing primary keys", "Creating HTML pages"], 1),
        _q("databases", "expert", "Why might a schema intentionally denormalize some data?", ["To improve read performance or simplify frequent queries at the cost of extra redundancy", "To eliminate all storage", "To guarantee zero locking", "To remove foreign keys everywhere"], 1),
        _q("databases", "expert", "What is a deadlock in a transactional database?", ["Two or more transactions wait indefinitely for resources held by each other", "A table with no rows", "A failed SELECT syntax", "A database with too many columns"], 1),
    ],
    "machine learning": [
        _q("machine learning", "expert", "Which situation is a classic example of data leakage?", ["Fitting a preprocessing scaler on the full dataset before train-test splitting", "Using a separate test set", "Encoding labels consistently", "Shuffling training rows"], 1),
        _q("machine learning", "expert", "For a highly imbalanced classification problem, why can PR-AUC be more informative than accuracy?", ["It focuses on the precision-recall trade-off for the positive class", "It always produces a higher score", "It ignores false positives", "It is only for regression"], 1),
        _q("machine learning", "expert", "What does probability calibration address?", ["Whether predicted probabilities reflect observed event frequencies", "Whether features have column names", "Whether a model trains on GPUs", "Whether a dataset is sorted"], 1),
        _q("machine learning", "expert", "Why can nested cross-validation be used for model selection and performance estimation?", ["It separates hyperparameter selection from the outer evaluation loop", "It removes the need for any test data in all situations", "It guarantees perfect generalization", "It only works for clustering"], 1),
        _q("machine learning", "expert", "What is a major purpose of SHAP-style explanations?", ["Estimating how features contribute to an individual prediction", "Training a neural network faster", "Increasing dataset size", "Replacing the target variable"], 1),
    ],
}

for _skill, _expert_questions in EXPERT_QUESTION_BANK.items():
    QUESTION_BANK[_skill]["expert"] = _expert_questions

# Flattened list kept for compatibility with any older imports.
QUESTIONS = [
    question
    for skill_questions in QUESTION_BANK.values()
    for difficulty_questions in skill_questions.values()
    for question in difficulty_questions
]


def get_difficulty(confidence):
    """Convert a 1-5 confidence rating into an assessment difficulty band."""
    try:
        confidence = int(confidence)
    except (TypeError, ValueError):
        confidence = 3
    confidence = min(max(confidence, 1), 5)
    return DIFFICULTY_MAP[confidence]



def get_adaptive_questions(
    self_ratings,
    questions_per_skill=3,
    branch="CSE",
    semester=1,
):
    """Select questions using branch, confidence, and semester."""

    branch = str(branch).strip().upper()

    if branch not in BRANCH_SKILL_LABELS:
        raise ValueError("Branch must be CSE, ISE, or ECE.")

    skill_labels = BRANCH_SKILL_LABELS[branch]
    question_bank = ECE_QUESTION_BANK if branch == "ECE" else QUESTION_BANK

    semester = max(1, min(8, int(semester)))
    selected = []

    for skill in skill_labels:
        confidence = self_ratings.get(skill, 3)
        difficulty = get_difficulty(confidence)

        if semester <= 2 and difficulty in ("advanced", "expert"):
            difficulty = "intermediate"
        elif semester <= 4 and difficulty == "expert":
            difficulty = "advanced"

        skill_bank = question_bank.get(skill)

        if not skill_bank:
            raise ValueError(
                f"No question bank configured for {branch}: {skill}"
            )

        # Some ECE subjects have no expert questions yet.
        if difficulty not in skill_bank:
            difficulty = "advanced" if "advanced" in skill_bank else "intermediate"

        selected.extend(
            skill_bank[difficulty][:questions_per_skill]
        )

    return selected


def calculate_skill_scores(self_ratings, quiz_answers):
    """
    Combine perceived confidence and objective performance.

    Final score = 40% self-assessment + 60% objective assessment.
    Objective assessment is the percentage of correct answers out of
    the adaptive questions shown for each skill.
    """
    skill_results = {}

    # Score the skills included in this student's assessment.
    for skill in self_ratings:
        confidence = int(self_ratings.get(skill, 3))
        self_score = round((confidence / 5) * 100)

        skill_questions = quiz_answers.get(skill, [])
        if not skill_questions:
            objective_score = 0
            correct = 0
            total = 0
        else:
            correct = sum(1 for answer, question in skill_questions if answer == question["options"][question["answer"] - 1])
            total = len(skill_questions)
            objective_score = round((correct / total) * 100, 2) if total else 0

        final_score = round((0.40 * self_score) + (0.60 * objective_score), 2)

        if final_score >= 80:
            level = "Advanced"
        elif final_score >= 60:
            level = "Intermediate"
        elif final_score >= 40:
            level = "Basic"
        else:
            level = "Beginner"

        skill_results[skill] = {
            "self_score": self_score,
            "objective_score": objective_score,
            "score": final_score,
            "level": level,
            "difficulty": get_difficulty(confidence),
            "correct": correct,
            "total": total,
        }

    return skill_results


def conduct_assessment():
    """Console version kept for compatibility/testing outside Streamlit."""
    print("\n===================================")
    print("       ADAPTIVE SKILL ASSESSMENT")
    print("===================================\n")

    name = input("Enter your name: ").strip()
    self_ratings = {}
    for skill, label in SKILL_LABELS.items():
        while True:
            try:
                rating = int(input(f"Rate your confidence in {label} (1-5): "))
                if 1 <= rating <= 5:
                    self_ratings[skill] = rating
                    break
            except ValueError:
                pass
            print("Please enter a number from 1 to 5.")

    questions = get_adaptive_questions(self_ratings)
    quiz_answers = {skill: [] for skill in SKILL_LABELS}

    for index, question in enumerate(questions, start=1):
        print(f"\nQ{index}. [{question['difficulty'].title()} - {SKILL_LABELS[question['skill']]}] {question['question']}")
        for option_number, option in enumerate(question["options"], start=1):
            print(f"{option_number}. {option}")
        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
            except ValueError:
                pass
            print("Please enter a number between 1 and 4.")
        quiz_answers[question["skill"]].append((question["options"][answer - 1], question))

    results = calculate_skill_scores(self_ratings, quiz_answers)
    skill_scores = {skill: result["score"] for skill, result in results.items()}
    user_skills = [skill for skill, score in skill_scores.items() if score >= 60]

    return {
        "name": name,
        "skills": user_skills,
        "skill_scores": skill_scores,
        "skill_results": results,
    }


if __name__ == "__main__":
    profile = conduct_assessment()
    print("\nSkill Scores:")
    for skill, result in profile["skill_results"].items():
        print(f"- {SKILL_LABELS[skill]}: {result['score']}% ({result['level']})")
