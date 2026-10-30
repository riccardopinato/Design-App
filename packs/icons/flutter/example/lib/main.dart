import 'package:factory_icons/factory_icons.dart';
import 'package:flutter/material.dart';

void main() => runApp(const FactoryIconsShowcase());

class FactoryIconsShowcase extends StatefulWidget {
  const FactoryIconsShowcase({super.key});

  @override
  State<FactoryIconsShowcase> createState() => _FactoryIconsShowcaseState();
}

class _FactoryIconsShowcaseState extends State<FactoryIconsShowcase> {
  bool dark = false;
  int taps = 0;

  @override
  Widget build(BuildContext context) => MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.pink),
        darkTheme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.pink,
            brightness: Brightness.dark,
          ),
        ),
        themeMode: dark ? ThemeMode.dark : ThemeMode.light,
        home: Scaffold(
          appBar: AppBar(title: const Text('Factory Icons — 24 keys')),
          body: ListView(
            padding: const EdgeInsets.all(16),
            children: [
              SwitchListTile(
                title: const Text('Dark theme'),
                value: dark,
                onChanged: (value) => setState(() => dark = value),
              ),
              Text('Button taps: $taps'),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final icon in FactoryIconKey.values)
                    Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        FactoryIconButton(
                          icon: icon,
                          tooltip: 'Preview ${icon.name}',
                          onPressed: () => setState(() => taps++),
                        ),
                        Text(icon.name, style: const TextStyle(fontSize: 10)),
                      ],
                    ),
                ],
              ),
            ],
          ),
        ),
      );
}
