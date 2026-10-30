import 'package:factory_visual_qa/factory_visual_qa.dart';
import 'package:flutter/material.dart';

void main() => runApp(const VisualQaShowcase());

class VisualQaShowcase extends StatefulWidget {
  const VisualQaShowcase({super.key});

  @override
  State<VisualQaShowcase> createState() => _VisualQaShowcaseState();
}

class _VisualQaShowcaseState extends State<VisualQaShowcase> {
  bool dark = false;
  bool adSlot = false;
  bool longLocale = false;
  QaUiState state = QaUiState.content;

  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'Factory Visual QA',
        theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
        darkTheme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.indigo,
            brightness: Brightness.dark,
          ),
        ),
        themeMode: dark ? ThemeMode.dark : ThemeMode.light,
        home: Scaffold(
          appBar: AppBar(title: const Text('QA scenario controls')),
          body: Column(
            children: [
              SwitchListTile(
                title: const Text('Dark'),
                value: dark,
                onChanged: (value) => setState(() => dark = value),
              ),
              SwitchListTile(
                title: const Text('Reserved banner'),
                value: adSlot,
                onChanged: (value) => setState(() => adSlot = value),
              ),
              SwitchListTile(
                title: const Text('Long localization'),
                value: longLocale,
                onChanged: (value) => setState(() => longLocale = value),
              ),
              DropdownButton<QaUiState>(
                value: state,
                items: [
                  for (final option in QaUiState.values)
                    DropdownMenuItem(value: option, child: Text(option.name)),
                ],
                onChanged: (value) =>
                    setState(() => state = value ?? QaUiState.content),
              ),
              Expanded(
                child: QaFixture(
                  state: state,
                  withAdSlot: adSlot,
                  longLocale: longLocale,
                ),
              ),
            ],
          ),
        ),
      );
}
